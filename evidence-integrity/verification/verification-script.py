#!/usr/bin/env python3

import hashlib
import sys
from pathlib import Path

def calculate_hash(path):
    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def verify(original, copy):
    original_hash = calculate_hash(original)
    copy_hash = calculate_hash(copy)

    print(f"Original SHA-256: {original_hash}")
    print(f"Copy SHA-256:     {copy_hash}")

    if original_hash == copy_hash:
        print("RESULT: PASS - Files match")
        return True

    print("RESULT: FAIL - Integrity mismatch")
    return False


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 verification-script.py ORIGINAL COPY")
        sys.exit(2)

    sys.exit(0 if verify(Path(sys.argv[1]), Path(sys.argv[2])) else 1)
