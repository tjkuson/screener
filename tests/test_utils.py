"""Test utils module; for use with `pytest`."""

from __future__ import annotations

from pathlib import Path
from screener.checker import Checker

from screener.utils import (
    html_contains_images_with_external_sources,
    html_contains_javascript,
)


class TestUtilFunctions:
    """Test utility functions."""

    test_dir = Path(__file__).parent

    def test_html_contains_javascript(self) -> None:
        """Test html_contains_javascript function."""
        # Check function returns False when there are no script tags.
        safe_html = self.test_dir / "safe.html"
        safe_html_checker = Checker(safe_html)
        with safe_html.open("rb") as file:
            content = file.read()
            assert html_contains_javascript(safe_html_checker, content) is None

        # Check function returns True when there are script tags.
        html_with_script_tags = self.test_dir / "script_tags.html"
        html_with_script_tags_checker = Checker(html_with_script_tags)
        with html_with_script_tags.open("rb") as file:
            content = file.read()
            diagnostics = html_contains_javascript(
                html_with_script_tags_checker, content
            )
            assert diagnostics is not None
            assert len(diagnostics) == 1

    def test_html_contains_images_with_external_sources(self) -> None:
        """Test html_contains_images_with_external_sources function."""
        # Check function returns False when there are external images.
        safe_html = self.test_dir / "safe_image.html"
        safe_html_checker = Checker(safe_html)
        with safe_html.open("rb") as file:
            content = file.read()
            assert (
                html_contains_images_with_external_sources(safe_html_checker, content)
                is None
            )

        # Check function returns True when there are external images.
        html_with_external_image = self.test_dir / "unsafe_image.html"
        html_with_external_image_checker = Checker(html_with_external_image)
        with html_with_external_image.open("rb") as file:
            content = file.read()
            diagnostics = html_contains_images_with_external_sources(
                html_with_external_image_checker, content
            )
            assert diagnostics is not None
            assert len(diagnostics) == 1
