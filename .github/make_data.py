#!/usr/bin/env python3

import json
import requests
import typing as t
from pathlib import Path

# TODO: make url dynamic once we moved PopTracker to the org
latest_release_url = "https://api.github.com/repos/black-sliver/Poptracker/releases/latest"
newest_releases_url = "https://api.github.com/repos/black-sliver/Poptracker/releases?per_page=1"
changelog_base_url = "https://github.com/black-sliver/PopTracker/blob/master/CHANGELOG.md"
# TODO: maybe copy changelog into the site instead of linking to it


def extract_data(data: dict[str, t.Any]) -> dict[str, str]:
    version: str = data["tag_name"]
    url: str = data["html_url"]
    changelog_tag = version.replace(".", "").replace(" ", "-")

    downloads: dict[str, str] = {}
    sigs: dict[str, str] = {}

    for asset in data["assets"]:
        assert isinstance(asset, dict)
        name: str = asset["name"]
        download: str = asset["browser_download_url"]
        if name.endswith(".AppImage"):
            downloads["appimage"] = download
        elif name.endswith(".AppImage.minisig"):
            sigs["appimage"] = download
        elif name.endswith("-source.tar.xz"):
            downloads["source"] = download
        elif name.endswith("-source.tar.xz.minisig"):
            sigs["source"] = download
        elif name.endswith("_macos.zip"):
            downloads["macos"] = download
        elif name.endswith("_macos.zip.minisig"):
            sigs["macos"] = download
        elif "_ubuntu" in name and name.endswith(".tar.xz"):
            downloads["linux"] = download
        elif "_ubuntu" in name and name.endswith(".tar.xz.minisig"):
            sigs["linux"] = download
        elif name.endswith("_win64.zip"):
            downloads["windows"] = download
        elif name.endswith("_win64.zip.minisig"):
            sigs["windows"] = download

    res = {"version": version, "url": url, "changelog": f"{changelog_base_url}#{changelog_tag}"}

    for download_type in ("windows", "macos", "appimage", "linux", "source"):
        if download_type not in downloads:
            raise ValueError(f"Download for {download_type} missing from release in {version}")
        if download_type not in sigs:
            raise ValueError(f"Signature for {download_type} missing from release in {version}")
        res[f"{download_type}_download"] = downloads[download_type]

    return res


def main() -> None:
    latest_json = requests.get(latest_release_url).json()
    newest_json = requests.get(newest_releases_url).json()[0]

    latest_data = extract_data(latest_json)
    newest_data = extract_data(newest_json)

    next_data = newest_data if newest_data["version"] != latest_data["version"] else {}

    repo_root = Path(__file__).parent.parent
    latest_path = repo_root / "_data" / "releases" / "latest.json"
    next_path = repo_root / "_data" / "releases" / "next.json"

    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump(latest_data, f)

    with open(next_path, "w", encoding="utf-8") as f:
        json.dump(next_data, f)


if __name__ == "__main__":
    main()
