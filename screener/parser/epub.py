"""Parse epub file to check that it is safe."""

from pathlib import Path

from ebooklib import ITEM_DOCUMENT

from screener.checker import Checker
from screener.diagnostic import ExternalImageDiagnostic, JavaScriptDiagnostic
from screener.reader import EpubFileReader
from screener.utils import (
    html_contains_images_with_external_sources,
    html_contains_javascript,
)


def parse_epub(
    checker: Checker,
    path_to_epub: Path,
) -> None:
    """Parse epub to check that it is safe.

    Mutates the checker object to add diagnostics.
    """
    with EpubFileReader(path_to_epub) as epub:
        for item in epub.book.get_items_of_type(ITEM_DOCUMENT):
            content = item.get_content()
            if diagnostics := html_contains_javascript(checker, content):
                checker.diagnostics.extend(diagnostics)
            if diagnostics := html_contains_images_with_external_sources(
                checker, content
            ):
                checker.diagnostics.extend(diagnostics)
