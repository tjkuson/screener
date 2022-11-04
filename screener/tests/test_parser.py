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
Test the parser module; for use with `pytest`.
"""

from pathlib import Path

from screener.parser.epub import parse_epub
from screener.parser.kindle import parse_kindle

TEST_DIR = Path(__file__).parent


def test_parse_epub():
    """Test epub file."""

    safe_epub_file = TEST_DIR / "william-shakespeare_richard-ii.epub"
    assert parse_epub(safe_epub_file)

    unsafe_epub_file = TEST_DIR / "william-shakespeare_richard-ii_with-script-tags.epub"
    assert not parse_epub(unsafe_epub_file)


def test_parse_kindle():
    """Test kindle file."""

    safe_kindle_file = TEST_DIR / "laozi_tao-te-ching_james-legge.azw3"
    assert parse_kindle(safe_kindle_file)

    unsafe_kindle_file = (
        TEST_DIR / "laozi_tao-te-ching_james-legge_with-script-tags.azw3"
    )
    assert not parse_kindle(unsafe_kindle_file)
