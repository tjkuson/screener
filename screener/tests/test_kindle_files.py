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

""" Screener tests

Test the Kindle file functionality of the screener module; for use with `pytest`.
"""

from os.path import abspath, dirname, join
from pathlib import Path

from ..kindle import InterpretKindleFile
from ..screener import epub_safe

TEST_DIR = dirname(abspath(__file__))


def test_parse_azw3() -> None:
    """Test azw3 file."""
    temp_dir: Path
    epub_translation: Path

    safe_azw3_file: Path = Path(join(TEST_DIR, "laozi_tao-te-ching_james-legge.azw3"))
    with InterpretKindleFile(safe_azw3_file) as interpretation:
        temp_dir = Path(interpretation.temp_dir)
        epub_translation = Path(interpretation.generated_epub)
        assert epub_translation.exists()
        assert temp_dir.exists()
        assert epub_safe(epub_translation)
    assert not epub_translation.exists()
    assert not temp_dir.exists()

    unsafe_azw3_file: Path = Path(
        join(TEST_DIR, "laozi_tao-te-ching_james-legge_with-script-tags.azw3")
    )
    with InterpretKindleFile(unsafe_azw3_file) as interpretation:
        temp_dir = Path(interpretation.temp_dir)
        epub_translation = Path(interpretation.generated_epub)
        assert epub_translation.exists()
        assert temp_dir.exists()
        assert not epub_safe(epub_translation)
    assert not epub_translation.exists()
    assert not temp_dir.exists()
