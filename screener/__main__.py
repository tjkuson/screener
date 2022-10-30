"""Screener entry-point script."""

import sys
from argparse import ArgumentParser, Namespace

from .screener import epub_safe, init_argparse


def main() -> None:
    """Read system args and check e-book files."""

    parser: ArgumentParser = init_argparse()
    args: Namespace = parser.parse_args()
    if not args.files:
        print("no file input")
    for file in args.files:
        if file == "-":
            continue
        try:
            if epub_safe(file):
                print(f"No JavaScript detected in {file}")
            else:
                print(f"JavaScript detected in {file}!")
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()
