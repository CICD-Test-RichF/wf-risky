"""Tiny placeholder app so code scanning has something to analyze."""

import sys


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(f"hello {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
