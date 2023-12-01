"""Parse ebook files in different formats."""

from .epub import parse_epub
from .kindle import parse_kindle

__all__ = ("parse_epub", "parse_kindle")
