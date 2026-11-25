#!/usr/bin/env python3

import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone


def calculate_sha256(file_path):
    digest = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)

    return digest.hexdigest()


def compare_files(original, working_copy):
    original_hash = calculate_sha256(original)
    working_hash = calculate_sha256(working_copy)

    return {
        "original": str(original),
        "working_copy": str(working_copy),
        "original_sha256": original_hash,
        "working_sha256": working_hash,
        "match": original_hash == working_hash,
    }


def main():
    parser = argparse.ArgumentParser(
        description="DFIR file integrity validation tool"
    )
    parser.add_argument("original", help="Original evidence file")
    parser.add_argument("working_copy", help="Working copy file")
    parser.add_argument("--output", help="Optional JSON report path")

    args = parser.parse_args()

    original = Path(args.original)
    working_copy = Path(args.working_copy)

    if not original.is_file() or not working_copy.is_file():
        parser.error("Both input paths must be existing files")

    result = compare_files(original, working_copy)
    result["generated_utc"] = datetime.now(timezone.utc).isoformat()

    report = json.dumps(result, indent=4)

    if args.output:
        Path(args.output).write_text(report + "\n", encoding="utf-8")

    print(report)

    return 0 if result["match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
