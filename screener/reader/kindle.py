"""Contains methods to check a Kindle e-book file for security and privacy issues."""

from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from types import TracebackType

from mobi import extract

from .abstract import AbstractReader


class KindleFileReader(AbstractReader):
    """Handle azw3 files."""

    def __init__(self: KindleFileReader, file_path: Path) -> None:
        """Initialize the class."""
        super().__init__(file_path)
        self._temp_dir: Path
        self.generated_translation: Path

    def __enter__(self: KindleFileReader) -> KindleFileReader:
        """Runtime context."""
        # The `mobi` library likes file paths as strings for whatever reason.
        self._temp_dir, self.generated_translation = extract(str(self.file_path))
        # The 'with' statement binds the object to its 'as' clause (if specified).
        return self

    def __exit__(
        self: KindleFileReader,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Delete temp files."""
        shutil.rmtree(self._temp_dir)
