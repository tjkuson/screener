"""Test utils module; for use with `pytest`."""

from __future__ import annotations

from pathlib import Path

from screener.utils import (
    html_contains_images_with_external_sources,
    html_contains_javascript,
)


class TestUtilFunctions:
    """Test utility functions."""

    test_dir = Path(__file__).parent

    def test_html_contains_javascript(self: TestUtilFunctions) -> None:
        """Test html_contains_javascript function."""
        # Check function returns False when there are no script tags
        safe_html = self.test_dir / "safe.html"
        with safe_html.open("rb") as file:
            content: bytes = file.read()
            assert not html_contains_javascript(content)

        # Check function returns True when there are script tags
        html_with_script_tags = self.test_dir / "script_tags.html"
        with html_with_script_tags.open("rb") as file:
            content = file.read()
            assert html_contains_javascript(content)

    def test_html_contains_images_with_external_sources(
        self: TestUtilFunctions,
    ) -> None:
        """Test html_contains_images_with_external_sources function."""
        # Check function returns False when there are external images
        safe_html = self.test_dir / "safe_image.html"
        with safe_html.open("rb") as file:
            content = file.read()
            assert not html_contains_images_with_external_sources(content)

        # Check function returns True when there are external images
        html_with_external_image = self.test_dir / "unsafe_image.html"
        with html_with_external_image.open("rb") as file:
            content = file.read()
            assert html_contains_images_with_external_sources(content)
