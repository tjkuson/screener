"""Screener entry-point script."""

import sys
from argparse import ArgumentParser
from pathlib import Path

from screener.checker import Checker
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
        version=f"{parser.prog} version 0.4.0",
    )
    parser.add_argument("files", nargs="*")
    return parser


def check_file(
    file: Path,
) -> Checker:
    """Check file."""
    extension = file.suffix
    checker = Checker(file)
    match extension:
        case ".epub":
            with EpubFileReader(file) as epub:
                parse_epub(checker, epub.file_path)
        case ".azw3" | ".mobi":
            with KindleFileReader(file) as azw3:
                parse_kindle(checker, azw3.file_path)
        case _:
            msg = f"unsupported file extension: {extension}"
            raise ValueError(msg)
    return checker


def main() -> None:
    """Read system args and check e-book files."""
    parser = init_argparse()
    args = parser.parse_args()
    if not args.files:
        print("No files specified. Run with -h for help.", file=sys.stderr)
    for file in args.files:
        if file == "-":
            print("stdin not supported", file=sys.stderr)
            continue
        checker = check_file(Path(file))
        if checker.diagnostics:
            for diagnostic in checker.diagnostics:
                print(diagnostic)
            sys.exit(1)
        print(f"{checker.file_path.name} is safe")

    sys.exit()


if __name__ == "__main__":
    main()
