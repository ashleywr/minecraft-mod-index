#!/usr/bin/env python3
"""Refresh the public Minecraft mod index from GitHub and runtime JAR metadata."""
import argparse
import concurrent.futures
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import tomllib
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CORE = {"minecraft", "java", "fabricloader", "neoforge", "forge"}
RUNTIME = re.compile(r"(?i)(?:^|[-.])(?:sources?|javadoc|dev|slim|common|tests?)(?:[-.]|$)")


def get_json(url, token=None):
    headers = {"User-Agent": "ashleywr-minecraft-mod-index/1", "Accept": "application/vnd.github+json"}
    if token:
        # Credentials are sent only to GitHub's API, never to asset/CDN URLs.
        if not url.startswith("https://api.github.com/"):
            raise ValueError("Refusing credentials outside the GitHub API")
        headers["Authorization"] = "Bearer " + token
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90) as response:
        return json.load(response)


def gh_json(path, token=None):
    return get_json("https://api.github.com/" + path, token)


def dep(mod_id, version="*", kind="required", side="BOTH", reason="", evidence="JAR metadata"):
    return dict(id=mod_id, version=version, kind=kind, side=side, reason=reason, evidence=evidence)


def parse_jar(path):
    """Read required/optional/conflicting deps, including embedded-mod identities."""
    variants = []
    with zipfile.ZipFile(path) as jar:
        names = set(jar.namelist())
        bundled = set()
        for name in sorted(names):
            if name.endswith(".jar") and name.startswith("META-INF/"):
                try:
                    for variant in parse_jar(io.BytesIO(jar.read(name))):
                        bundled.update(variant["mod_ids"])
                except (zipfile.BadZipFile, KeyError, tomllib.TOMLDecodeError, json.JSONDecodeError):
                    pass  # A library may not be a Minecraft mod.
        java_majors = []
        for name in names:
            if name.endswith(".class") and not name.startswith("META-INF/versions/"):
                with jar.open(name) as entry:
                    header = entry.read(8)
                if header[:4] == b"\xca\xfe\xba\xbe":
                    java_majors.append(int.from_bytes(header[6:8], "big"))
        java_min = max(java_majors, default=0) - 44
        if "fabric.mod.json" in names:
            data = json.loads(jar.read("fabric.mod.json"))
            deps = []
            for key, kind in (("depends", "required"), ("recommends", "recommended"), ("suggests", "optional"), ("breaks", "incompatible"), ("conflicts", "discouraged")):
                for mod_id, version in data.get(key, {}).items():
                    deps.append(dep(mod_id, version, kind))
            variants.append(dict(loader="Fabric", mod_ids=[data["id"]], version=data["version"],
                                 minecraft=data.get("depends", {}).get("minecraft", "not declared"),
                                 environment=data.get("environment", "*"), dependencies=deps))
        for filename, loader in (("META-INF/neoforge.mods.toml", "NeoForge"), ("META-INF/mods.toml", "Forge")):
            if filename not in names:
                continue
            data = tomllib.loads(jar.read(filename).decode("utf-8"))
            mod_ids = [mod["modId"] for mod in data.get("mods", [])]
            deps = []
            for group in data.get("dependencies", {}).values():
                for item in group:
                    kind = item.get("type", "required" if item.get("mandatory", True) else "optional")
                    value = dep(item["modId"], item.get("versionRange", "*"), kind,
                                item.get("side", "BOTH"), item.get("reason", ""))
                    if value not in deps:
                        deps.append(value)
            variants.append(dict(loader=loader, mod_ids=mod_ids,
                                 version=", ".join(str(mod.get("version", "unspecified")) for mod in data.get("mods", [])),
                                 minecraft=next((d["version"] for d in deps if d["id"] == "minecraft"), "not declared"),
                                 environment="see dependency sides", dependencies=deps))
        for variant in variants:
            if java_min > 0 and not any(d["id"] == "java" for d in variant["dependencies"]):
                variant["dependencies"].append(dep("java", ">=" + str(java_min), evidence="runtime class-file version"))
            for item in variant["dependencies"]:
                item["bundled"] = item["id"] in bundled or item["id"] in variant["mod_ids"]
            variant["bundled_mods"] = sorted(bundled)
    return variants


def enrich(variants, project):
    # Reviewed source-derived requirements fill known omissions in loader manifests.
    for variant in variants:
        for extra in project.get("additional_requirements", []):
            if extra.get("loader", variant["loader"]) == variant["loader"]:
                value = {k: v for k, v in extra.items() if k != "loader"}
                if not any(d["id"] == value["id"] and d["kind"] == value["kind"] for d in variant["dependencies"]):
                    variant["dependencies"].append(dict(value, bundled=False))
    return variants


def refresh_project(project, token, cache, local_artifacts):
    result = dict(project)
    repository = project.get("repository")
    if repository:
        branch = project["branch"]
        commit = gh_json("repos/" + repository + "/commits/" + urllib.parse.quote(branch, safe=""), token)
        result["source_update"] = dict(date=commit["commit"]["committer"]["date"], sha=commit["sha"], url=commit["html_url"])
    if project["status"] != "published":
        result["artifacts"] = project["snapshot"]["artifacts"]
        return result
    # Include prereleases, but never drafts or development/source-only attachments.
    releases = gh_json("repos/" + repository + "/releases?per_page=100", token)
    releases = [r for r in releases if not r["draft"] and r.get("published_at") and
                any(a["name"].endswith(".jar") and not RUNTIME.search(a["name"]) for a in r["assets"])]
    if not releases:
        raise RuntimeError(repository + ": no published runtime JAR release")
    release = max(releases, key=lambda r: r["published_at"])
    result["release"] = dict(tag=release["tag_name"], date=release["published_at"],
                             url=release["html_url"], prerelease=release["prerelease"])
    result["artifacts"] = []
    for asset in release["assets"]:
        name = asset["name"]
        if not name.endswith(".jar") or RUNTIME.search(name):
            continue
        url = asset["browser_download_url"]
        local_path = local_artifacts.get(urllib.parse.unquote(url))
        if local_path:
            candidate = Path(local_path)
            # A local rebuild may have replaced the audited file at the same path.
            valid = candidate.exists() and candidate.stat().st_size == asset["size"]
            if valid and asset.get("digest"):
                with candidate.open("rb") as source:
                    valid = asset["digest"] == "sha256:" + hashlib.file_digest(source, "sha256").hexdigest()
            if not valid:
                local_path = None
        path = Path(local_path) if local_path else cache / (str(asset["id"]) + ".jar")
        if not path.exists():
            request = urllib.request.Request(url, headers={"User-Agent": "ashleywr-minecraft-mod-index/1"})
            temporary = path.with_suffix(".part")
            with urllib.request.urlopen(request, timeout=180) as response, temporary.open("wb") as output:
                while chunk := response.read(1024 * 1024):
                    output.write(chunk)
            temporary.replace(path)
        with path.open("rb") as source:
            digest = hashlib.file_digest(source, "sha256").hexdigest()
        if asset.get("digest") and asset["digest"] != "sha256:" + digest:
            raise RuntimeError(repository + ": SHA-256 mismatch for " + name)
        if path.stat().st_size != asset["size"]:
            raise RuntimeError(repository + ": size mismatch for " + name)
        variants = enrich(parse_jar(path), project)
        if not variants:
            raise RuntimeError(repository + ": no loader metadata in " + name)
        result["artifacts"].append(dict(name=name, url=url, bytes=asset["size"], sha256=digest, variants=variants))
    return result


def escaped(value):
    return str(value).replace("|", "&#124;").replace("\n", " ")


def code(value):
    return "`" + escaped(json.dumps(value) if isinstance(value, list) else value) + "`"


def dep_text(item, links):
    info = links.get(item["id"], {})
    label = info.get("name", item["id"])
    name = "[" + label + "](" + info["url"] + ")" if info.get("url") else code(label)
    text = name + " " + code(item["version"])
    if item.get("side") not in ("BOTH", None):
        text += " (" + item["side"].lower() + ")"
    if item.get("bundled"):
        text += " (included)"
    if item.get("evidence") != "JAR metadata":
        text += " (" + escaped(item["evidence"]) + ")"
    if item.get("reason"):
        text += " — " + escaped(item["reason"])
    return text


def render(catalog, links):
    projects = catalog["projects"]
    published = sum(p["status"] == "published" for p in projects)
    held = sum(p["status"] == "source-only" for p in projects)
    local_builds = sum(p["status"] == "local-build" for p in projects)
    lines = ["# My Minecraft Mod Index", "",
             "Automation-assisted Minecraft mod ports, upgrades, compatibility fixes and original mods — in one searchable place.", "",
             f"**{len(projects)} projects · {published} with public JAR downloads · {held} source-only entries · {local_builds} local snapshots without public JARs.**", "",
             "Index checked: **" + catalog["checked_at"][:10] + " (UTC)**. Source dates are the latest commits on the listed maintained branches; release dates are when GitHub published the selected JAR release. A documentation-only commit can change a source date. Dates do not promise ongoing maintenance.", "",
             "Search this page with your browser's Find, or search this repository on GitHub for a mod name, dependency ID, Minecraft version or loader. Each entry has exact JAR links and version-specific requirements. [Machine-readable catalog](catalog.json) · [Project list](projects.json) · [Refresh instructions](#updating-this-index).", "",
             "Forks and ports are unofficial. Original authors retain credit and ownership; listing a project here does not mean I created the original mod or its original port. The work includes builds, compatibility fixes and ports. Botania is an unofficial build of the upstream porting snapshot; see its prerelease notes.", "",
             "## Downloads at a glance", "",
             "Choose the exact Minecraft version and loader in the JAR details. Required dependency links lead to the project or its releases; select a compatible file there. Optional integrations are listed separately. Embedded mods are marked **included**; they usually need no separate download. Dependencies can have their own dependencies.", "",
             "| Mod | Minecraft / loader | Source updated (UTC) | JAR release (UTC) | Downloads and requirements |",
             "| --- | --- | --- | --- | --- |"]
    for project in projects:
        slug = project["id"]
        platforms = sorted({v["loader"] + " " + str(v["minecraft"]) for a in project["artifacts"] for v in a["variants"]})
        source = project.get("source_update", {})
        source_date = "[" + source["date"][:10] + "](" + source["url"] + ")" if source.get("url") else source.get("date", "not public")[:10]
        if project["status"] == "published":
            release = project["release"]
            date = "[" + release["date"][:10] + "](" + release["url"] + ")" + (" (prerelease)" if release["prerelease"] else "")
            download = "[JARs + dependencies](#" + slug + ")"
        else:
            date = "No public build of this work"
            download = "[" + ("Source only" if project["status"] == "source-only" else "Local snapshot") + "](#" + slug + ")"
        lines.append("| [" + project["name"] + "](#" + slug + ") | " + escaped("; ".join(platforms)) + " | " + source_date + " | " + date + " | " + download + " |")
    lines += ["", "## Mod details", "", "Version ranges below are copied from each packaged mod's metadata. For example, `[x,)` means at least x, `[x]` means exactly x, and `[x,y)` means x inclusive through y exclusive. `*` means no version constraint was declared. A broad metadata range is not a claim that every version in it was tested. Java minimums without an explicit declaration are inferred from compiled class-file versions.", ""]
    for project in projects:
        lines += ['<a id="' + project["id"] + '"></a>', "", "### " + project["name"], "", project["description"], "",
                  "**" + project["kind"] + ".** [Source](" + project["source_url"] + ")" + (" · [Upstream](" + project["upstream"] + ")" if project.get("upstream") else "") + " · License: **" + project["license"] + "**.", ""]
        source = project.get("source_update", {})
        if source.get("date"):
            lines += ["Source updated: **" + source["date"][:10] + " UTC**; commit " + ("[" + source["sha"][:8] + "](" + source["url"] + ")" if source.get("url") else code(source["sha"][:8])) + ".", ""]
        if project["status"] == "published":
            release = project["release"]
            lines += ["JAR release: **" + release["date"][:10] + " UTC** · [" + release["tag"] + "](" + release["url"] + ")" + (" · **Prerelease**" if release["prerelease"] else "") + ".", ""]
        else:
            lines += ["**No public JAR for this work.** " + project["publication_note"], "", "The following requirements describe the local build checked on **" + project["snapshot"]["built_at"] + "**, at commit " + code(project["snapshot"]["commit"][:8]) + ".", ""]
        for note in project.get("notes", []):
            lines += ["**Note:** " + note, ""]
        for artifact in project["artifacts"]:
            label = "[" + artifact["name"] + "](" + artifact["url"] + ")" if artifact.get("url") else code(artifact["name"]) + " (local build; no download)"
            lines += ["#### " + label, ""]
            for variant in artifact["variants"]:
                lines += ["**" + variant["loader"] + " · Minecraft " + code(variant["minecraft"]) + " · Mod " + code(variant["version"]) + "**", ""]
                for title, kinds, core in (("Runtime", {"required"}, True), ("Required mods", {"required"}, False), ("Optional integrations", {"optional", "recommended"}, False), ("Conflicts / discouraged combinations", {"incompatible", "discouraged"}, False)):
                    items = [d for d in variant["dependencies"] if d["kind"] in kinds and (d["id"] in CORE) == core]
                    if items:
                        lines += ["- **" + title + ":** " + "; ".join(dep_text(d, links) for d in items) + "."]
                    elif title == "Required mods":
                        lines += ["- **Required mods:** none declared beyond the runtime above."]
                if variant.get("bundled_mods"):
                    lines += ["- **Embedded mods:** " + ", ".join(code(x) for x in variant["bundled_mods"]) + "."]
                lines += [""]
            if artifact.get("sha256"):
                lines += ["SHA-256: " + code(artifact["sha256"]) + ".", ""]
    lines += ["## Availability, credit and licenses", "",
              "All builds are offered **AS IS**, without warranty. Updates and support are best effort. Successful builds and archive checks do not establish compatibility with every modpack or gameplay path.", "",
              "Original mods remain under their original licenses and any separate asset terms. My original code is MIT where identified. The MIT license in this repository covers the index text and refresh code only; it does not relicense any listed mod. Follow each project's license and credits. Source-only entries intentionally have no link to an older fork binary that could be mistaken for the current build.", "",
              "This index covers the reviewed workspace projects. Koyo projects and the removed Controlify, Immersive Portals and Vanilla Vehicles projects are omitted. Other historical GitHub forks are not evidence of an automation-assisted port and are not automatically advertised here.", "",
              "## Updating this index", "",
              "Run the **Refresh mod index** workflow from this repository's Actions tab, or use Python 3.11+ locally:", "",
              "```sh", "python scripts/refresh.py", "```", "",
              "The refresh checks each curated source branch, selects its newest published GitHub release containing runtime JARs, verifies available GitHub SHA-256 digests, and reads dependencies from those JARs. Prereleases are labelled. It refreshes README.md and catalog.json together. GitHub API access uses GH_TOKEN when set, or the authenticated gh CLI locally. No background schedule is configured.", "",
              "To add a project, edit projects.json. Source-only/local snapshot requirements are recorded snapshots and need a new reviewed build to change; the refresh never publishes their JARs. Source-derived dependency corrections include their evidence. Dependency URLs live in dependencies.json. Review the generated diff before committing a local refresh.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-dir", type=Path, default=Path(tempfile.gettempdir()) / "minecraft-mod-index-cache")
    parser.add_argument("--local-artifacts", type=Path, help="Optional private URL-to-local-JAR map; never committed")
    args = parser.parse_args()
    args.cache_dir.mkdir(parents=True, exist_ok=True)
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            auth = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True)
            token = auth.stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            pass
    projects = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    links = json.loads((ROOT / "dependencies.json").read_text(encoding="utf-8"))
    local = {urllib.parse.unquote(k): v for k, v in json.loads(args.local_artifacts.read_text(encoding="utf-8")).items()} if args.local_artifacts else {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda p: refresh_project(p, token, args.cache_dir, local), projects))
    results.sort(key=lambda p: p["name"].casefold())
    catalog = dict(schema_version=1, checked_at=dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), projects=results)
    # Build both outputs fully before replacing either; a failed refresh leaves the old index intact.
    markdown = render(catalog, links)
    json_text = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"
    (ROOT / "README.md").write_text(markdown, encoding="utf-8")
    (ROOT / "catalog.json").write_text(json_text, encoding="utf-8")
    print(f"Refreshed {len(results)} projects; {sum(p['status']=='published' for p in results)} public releases.")


if __name__ == "__main__":
    main()
