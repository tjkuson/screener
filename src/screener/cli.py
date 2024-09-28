from __future__ import annotations

import sys
from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING

from screener.checker import Checker
from screener.parser import parse_epub, parse_kindle
from screener.reader import EpubFileReader, KindleFileReader

if TYPE_CHECKING:
    from collections.abc import Sequence


def check_file(file: Path) -> Checker:
    checker = Checker(file)
    match extension := file.suffix:
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = ArgumentParser(
        prog="screener",
        usage="%(prog)s [OPTION] [FILE]...",
        description="Check e-book files for security and privacy issues.",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{parser.prog} version 0.5.0",
    )
    parser.add_argument("files", nargs="*")
    args = parser.parse_args(argv)
    if not args.files:
        print("No files specified. Run with -h for help.", file=sys.stderr)
    exit_code = 0
    for file in args.files:
        if file == "-":
            print("stdin not supported", file=sys.stderr)
            continue
        checker = check_file(Path(file))
        if checker.diagnostics:
            exit_code = 1
            for diagnostic in checker.diagnostics:
                print(diagnostic)
        else:
            print(f"{checker.file_path.name} is safe")

    return exit_code
