from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

from ebooklib import epub

from .abstract import AbstractReader


class EpubFileReader(AbstractReader):
    def __init__(self: EpubFileReader, file_path: Path) -> None:
        super().__init__(file_path)
        self.book: epub.EpubBook

    def __enter__(self: EpubFileReader) -> EpubFileReader:
        with warnings.catch_warnings():
            # Have to do this because of bug in ebooklib.
            warnings.simplefilter("ignore")
            self.book = epub.read_epub(self.file_path, options={"ignore_ncx": False})
        return self
