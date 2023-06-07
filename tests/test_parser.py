"""Test the parser module; for use with `pytest`."""

from __future__ import annotations

from pathlib import Path

from screener.diagnostic import (
    JavaScriptDiagnostic,
)
from screener.parser import parse_epub, parse_kindle


class TestParser:
    """Test the parser module."""

    # TODO: Test the parser for ebooks with image tags
    test_dir = Path(__file__).parent

    def test_parse_epub(self) -> None:
        """Test epub file."""
        safe_epub_file = self.test_dir / "william-shakespeare_richard-ii.epub"
        assert parse_epub(safe_epub_file) is None
        unsafe_epub_file = (
            self.test_dir / "william-shakespeare_richard-ii_with-script-tags.epub"
        )
        assert parse_epub(unsafe_epub_file) == JavaScriptDiagnostic(
            unsafe_epub_file.name
        )

    def test_parse_azw3(self: TestParser) -> None:
        """Test azw3 file."""
        safe_kindle_file = self.test_dir / "laozi_tao-te-ching_james-legge.azw3"
        assert parse_kindle(safe_kindle_file) is None
        unsafe_kindle_file = (
            self.test_dir / "laozi_tao-te-ching_james-legge_with-script-tags.azw3"
        )
        assert parse_kindle(unsafe_kindle_file) == JavaScriptDiagnostic(
            unsafe_kindle_file.name
        )

    def test_parse_mobi(self: TestParser) -> None:
        """Test mobi file."""
        # mobi files don't support JavaScript, so they are always safe (wrt script tags)
        safe_kindle_file = self.test_dir / "edith-wharton_ethan-frome.mobi"
        assert parse_kindle(safe_kindle_file) is None
