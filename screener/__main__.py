"""Screener entry-point script."""

import sys
from argparse import ArgumentParser
from pathlib import Path

from screener.parser import parse_epub, parse_kindle
from screener.reader import EpubFileReader, KindleFileReader


def init_argparse() -> ArgumentParser:
    """Create argument parser for system args."""
    parser = ArgumentParser(
        prog="screener",
        usage="%(prog)s [OPTION] [FILE]...",
        description="Check e-book files for security and privacy issues.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{parser.prog} version 0.2.3",
    )
    parser.add_argument("files", nargs="*")
    return parser


def main() -> None:
    """Read system args and check e-book files."""
    parser = init_argparse()
    args = parser.parse_args()
    if not args.files:
        print("no file input")
    for file in args.files:
        if file == "-":
            print("stdin not supported")
            continue
        try:
            extension = Path(file).suffix
            is_safe = True
            match extension:
                case ".epub":
                    with EpubFileReader(file) as epub:
                        is_safe = parse_epub(epub.file_path)
                case ".azw3", ".mobi":
                    with KindleFileReader(file) as azw3:
                        is_safe = parse_kindle(azw3.file_path)
            if is_safe:
                print(f"No JavaScript/external images detected in {file}")
            else:
                print(f"JavaScript/external images detected in {file}!")
        except (FileNotFoundError, IsADirectoryError) as exc:
            print(f"{sys.argv[0]}: {file}: {exc.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()
