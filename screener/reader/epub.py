from pathlib import Path

from ebooklib import epub

from .abstract import AbstractReader


class EpubFileReader(AbstractReader):
    """Handle epub files."""

    def __init__(self, file_path: Path) -> None:
        super().__init__(file_path)

    def __enter__(self):
        self.book: epub.EpubBook = epub.read_epub(self.file_path)
        return self
