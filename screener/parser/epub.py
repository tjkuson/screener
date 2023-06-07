"""Parse epub file to check that it is safe."""

from pathlib import Path

from ebooklib import ITEM_DOCUMENT

from screener.diagnostic import ExternalImageDiagnostic, JavaScriptDiagnostic
from screener.reader import EpubFileReader
from screener.utils import (
    html_contains_images_with_external_sources,
    html_contains_javascript,
)


def parse_epub(
    path_to_epub: Path,
) -> JavaScriptDiagnostic | ExternalImageDiagnostic | None:
    """Parse epub to check that it is safe."""
    with EpubFileReader(path_to_epub) as epub:
        for item in epub.book.get_items_of_type(ITEM_DOCUMENT):
            content = item.get_content()
            if html_contains_javascript(content):
                return JavaScriptDiagnostic(path_to_epub.name)
            if html_contains_images_with_external_sources(content):
                return ExternalImageDiagnostic(path_to_epub.name)
        return None
