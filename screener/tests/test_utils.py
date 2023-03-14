"""Test utils module; for use with `pytest`."""

from pathlib import Path

from screener.utils import (
    html_contains_images_with_external_sources,
    html_contains_javascript,
)

TEST_DIR = Path(__file__).parent


def test_html_contains_javascript() -> None:
    """Test html_contains_javascript function."""
    safe_html = TEST_DIR / "safe.html"
    with open(safe_html, "rb") as file:
        content: bytes = file.read()
        assert not html_contains_javascript(content)

    html_with_script_tags = TEST_DIR / "script_tags.html"
    with open(html_with_script_tags, "rb") as file:
        content = file.read()
        assert html_contains_javascript(content)


def test_html_contains_images_with_external_sources() -> None:
    """Test html_contains_images_with_external_sources function."""
    safe_html = TEST_DIR / "safe_image.html"
    with open(safe_html, "rb") as file:
        content: bytes = file.read()
        assert not html_contains_images_with_external_sources(content)

    html_with_external_image = TEST_DIR / "unsafe_image.html"
    with open(html_with_external_image, "rb") as file:
        content = file.read()
        assert html_contains_images_with_external_sources(content)
