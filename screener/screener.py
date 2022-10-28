# Screener: check e-book files for security issues.
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

"""Screener

Contains methods to check an e-book file for security and privacy issues.
"""

import logging
import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from bs4 import BeautifulSoup, ResultSet
from ebooklib import ITEM_DOCUMENT
from ebooklib.epub import EpubBook, read_epub


class Parser:
    """Define parser class that parses ebooks."""

    def __init__(self, content: bytes) -> None:
        """Store html file."""

        self.html = content

    def contains_javascript(self) -> bool:
        """Search for JavaScript in html files."""

        soup: BeautifulSoup = BeautifulSoup(self.html, "html.parser")
        scripts: ResultSet = soup.find_all("script")
        if scripts:
            logging.info("scripts detected: %s", scripts)
            return True
        return False


def epub_safe(path_to_epub: Path) -> bool:
    """Parse epub to check that it is safe."""

    book: EpubBook = read_epub(path_to_epub)
    contains_js: bool = False
    for item in book.get_items_of_type(ITEM_DOCUMENT):
        content: bytes = item.get_content()
        if Parser(content).contains_javascript():
            contains_js = True
    return not contains_js


def init_argparse() -> ArgumentParser:
    """Create argument parser for system args."""

    parser: ArgumentParser = ArgumentParser(
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
            # TODO: this isn't pretty; make this pretty and user-friendly.
            print(f"{epub_safe(file)=}")
        except (FileNotFoundError, IsADirectoryError) as err:
            print(f"{sys.argv[0]}: {file}: {err.strerror}", file=sys.stderr)


if __name__ == "__main__":
    main()
