"""Parse epub file to check that it is safe."""

from pathlib import Path

from ebooklib import ITEM_DOCUMENT

from screener.reader import EpubFileReader
from screener.utils import html_contains_javascript


def parse_epub(path_to_epub: Path) -> bool:
    """Parse epub to check that it is safe."""
    with EpubFileReader(path_to_epub) as epub:
        contains_js: bool = False

        for item in epub.book.get_items_of_type(ITEM_DOCUMENT):
            content: bytes = item.get_content()
            if html_contains_javascript(content):
                contains_js = True
        return not contains_js
