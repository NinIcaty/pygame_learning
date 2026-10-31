
#!/usr/bin/env python3

import argparse
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipapp

BOOTSTRAP = r'''
import sys
import os
import runpy
import zipfile
import hashlib
import pathlib
import platform

archive = pathlib.Path(sys.argv[0]).resolve()

# Unique cache for each build
digest = hashlib.sha256(archive.read_bytes()).hexdigest()[:16]

cache_id = (
    f"{digest}-{sys.version_info.major}.{sys.version_info.minor}-"
    f"{platform.system()}-{platform.machine()}"
)

cache_dir = pathlib.Path.home() / ".cache" / "pyz-pygame" / cache_id
marker = cache_dir / ".installed"

if not marker.exists():
    cache_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(archive) as z:
        members = [
            name for name in z.namelist()
            if name.startswith(("vendor/", "src/"))
        ]
        z.extractall(cache_dir, members)

    marker.touch()

sys.path.insert(0, str(cache_dir / "vendor"))
sys.path.insert(0, str(cache_dir / "src"))

runpy.run_path(
    str(cache_dir / "src" / "main.py"),
    run_name="__main__"
)
'''


def safe_name(value):
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", str(value).strip())
    value = value.strip(".-_")

    if not value:
        raise ValueError("Invalid filename component in metadata.json")

    return value


def build(source, metadata_file, output_dir):
    source = pathlib.Path(source).resolve()
    metadata_file = pathlib.Path(metadata_file).resolve()
    output_dir = pathlib.Path(output_dir).resolve()

    if not source.is_dir():
        raise SystemExit(f"Source folder not found: {source}")

    if not (source / "main.py").exists():
        raise SystemExit("src/main.py is required!")

    if not metadata_file.exists():
        raise SystemExit(f"Metadata not found: {metadata_file}")

    # Read metadata
    with metadata_file.open(encoding="utf-8") as f:
        metadata = json.load(f)

    version = safe_name(metadata["version"])
    build_number = safe_name(metadata["build"])

    # Automatically generate filename
    filename = f"topDown-{version}-{build_number}.pyz"
    output = output_dir / filename

    print(f"Building {filename}")
    print(f"Version: {version}")
    print(f"Build: {build_number}")

    with tempfile.TemporaryDirectory() as temp:
        temp = pathlib.Path(temp)

        # Copy source
        shutil.copytree(source, temp / "src")

        # Install pygame into bundle
        vendor = temp / "vendor"
        vendor.mkdir()

        print("\n[1/3] Bundling pygame...")

        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--upgrade",
                "--target",
                str(vendor),
                "pygame",
            ],
            check=True,
        )

        # Add bootstrapper
        print("\n[2/3] Adding bootstrapper...")

        (temp / "__main__.py").write_text(BOOTSTRAP)

        # Create archive
        print("\n[3/3] Creating PYZ...")

        output_dir.mkdir(parents=True, exist_ok=True)

        zipapp.create_archive(
            temp,
            output,
            interpreter="/usr/bin/env python3",
            compressed=True,
        )

    print(f"\nBuild successful!")
    print(f"Output: {output}")


if __name__ == "__main__":
    root = pathlib.Path(__file__).resolve().parent

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "source",
        nargs="?",
        default=str(root / "src")
    )

    parser.add_argument(
        "--metadata",
        default=str(root /"src"/ "metadata.json")
    )

    parser.add_argument(
        "--output-dir",
        default=str(root / "builds")
    )

    args = parser.parse_args()

    build(args.source, args.metadata, args.output_dir)
