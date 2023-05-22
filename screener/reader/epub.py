"""Read epub files."""

from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

from ebooklib import epub

from .abstract import AbstractReader


class EpubFileReader(AbstractReader):
    """Handle epub files."""

    def __init__(self: EpubFileReader, file_path: Path) -> None:
        """Initialize the class."""
        super().__init__(file_path)

    def __enter__(self: EpubFileReader) -> EpubFileReader:
        """Runtime context."""
        print("Reading epub file")
        with warnings.catch_warnings():
            # Have to do this because of bug in ebooklib
            warnings.simplefilter("ignore")
            self.book = epub.read_epub(self.file_path, options={"ignore_ncx": False})
        print("Finished reading epub file")
        return self
