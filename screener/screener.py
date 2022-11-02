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
Contains methods to check an e-book file for security and privacy issues.
"""

import logging
from argparse import ArgumentParser
from pathlib import Path

from bs4 import BeautifulSoup, ResultSet
from ebooklib import ITEM_DOCUMENT
from ebooklib.epub import EpubBook, read_epub


class Parser:
    """Define parser class that parses ebooks."""

    def __init__(self, content: bytes) -> None:
        """Store html file."""

        self.html: bytes = content

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
