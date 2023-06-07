"""Screener entry-point script."""

import sys
from argparse import ArgumentParser
from pathlib import Path

from screener.diagnostic import (
    ExternalImageDiagnostic,
    JavaScriptDiagnostic,
    ParseErrorDiagnostic,
)
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
        version=f"{parser.prog} version 0.3.0",
    )
    parser.add_argument("files", nargs="*")
    return parser


def check_file(
    file: Path,
) -> JavaScriptDiagnostic | ExternalImageDiagnostic | ParseErrorDiagnostic | None:
    """Check file."""
    try:
        extension = file.suffix
        match extension:
            case ".epub":
                with EpubFileReader(file) as epub:
                    return parse_epub(epub.file_path)
            case ".azw3", ".mobi":
                with KindleFileReader(file) as azw3:
                    return parse_kindle(azw3.file_path)
        return ParseErrorDiagnostic(file.name, f"unknown file extension: {extension}")
    except (FileNotFoundError, IsADirectoryError) as exc:
        print(f"{sys.argv[0]}: {file}: {exc.strerror}", file=sys.stderr)
        return ParseErrorDiagnostic(file.name, exc.strerror)


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
        diagnostic = check_file(Path(file))
        match diagnostic:
            case JavaScriptDiagnostic(file_path):
                print(f"{file_path}: contains JavaScript", file=sys.stderr)
            case ExternalImageDiagnostic(file_path):
                print(f"{file_path}: contains external images", file=sys.stderr)
            case ParseErrorDiagnostic(file_path, msg):
                print(f"{file_path}: could not be parsed ({msg})", file=sys.stderr)
            case None:
                print(f"{file}: safe", file=sys.stderr)


if __name__ == "__main__":
    main()
