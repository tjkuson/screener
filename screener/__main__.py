# Screener: check e-book files for security and privacy issues.
# Copyright (C) 2022 Tom Kuson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Screener entry-point script.
"""

import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from screener.parser.epub import parse_epub
from screener.parser.kindle import parse_kindle
from screener.reader.epub import EpubFileReader
from screener.reader.kindle import KindleFileReader


def init_argparse() -> ArgumentParser:
    """Create argument parser for system args."""

    parser: ArgumentParser = ArgumentParser(
        prog="screener",
        usage="%(prog)s [OPTION] [FILE]...",
        description="Check e-book files for security and privacy issues.",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} version 0.1.0"
    )
    parser.add_argument("files", nargs="*")
    return parser


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
            extension: str = Path(file).suffix
            is_safe: bool = True
            match extension:
                case ".epub":
                    with EpubFileReader(file) as epub:
                        is_safe = parse_epub(epub.file_path)
                case ".azw3", ".mobi":
                    with KindleFileReader(file) as azw3:
                        is_safe = parse_kindle(azw3.file_path)
            if is_safe:
                print(f"No JavaScript detected in {file}")
            else:
                print(f"JavaScript detected in {file}!")
        except (FileNotFoundError, IsADirectoryError) as exc:
            print(f"{sys.argv[0]}: {file}: {exc.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()
