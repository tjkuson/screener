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

""" Screener tests

Test the screener module; for use with `pytest`.
"""

from pathlib import Path

from ..screener import epub_safe


def test_contains_javascript():
    """Test that script can pick up a <script> tag in epub file."""
    safe_ebook_path = Path(r"screener/tests/william-shakespeare_richard-ii.epub")
    assert epub_safe(safe_ebook_path)
    unsafe_ebook_path = Path(
        r"screener/tests/william-shakespeare_richard-ii_with-script-tags.epub"
    )
    assert not epub_safe(unsafe_ebook_path)
