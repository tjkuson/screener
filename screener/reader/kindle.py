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
Contains methods to check a Kindle e-book file for security and privacy issues.
"""

import shutil
from pathlib import Path

import mobi

from .abstract import AbstractReader


class KindleFileReader(AbstractReader):
    """Handle azw3 files."""

    def __init__(self, file_path: Path) -> None:
        super().__init__(file_path)
        self._temp_dir: Path
        self.generated_epub: Path

    def __enter__(self):
        """The runtime context of the database class (connecting to the database)."""

        # The `mobi` library likes file paths as strings for whatever reason.
        self._temp_dir, self.generated_epub = mobi.extract(str(self.file_path))
        # The 'with' statement binds the object to its 'as' clause (if specified).
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Delete temp files."""
        shutil.rmtree(self._temp_dir)
