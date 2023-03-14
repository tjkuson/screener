"""Test the parser module; for use with `pytest`."""

from pathlib import Path

from screener.parser import parse_epub, parse_kindle

TEST_DIR = Path(__file__).parent


def test_parse_epub() -> None:
    """Test epub file."""
    safe_epub_file = TEST_DIR / "william-shakespeare_richard-ii.epub"
    assert parse_epub(safe_epub_file)

    unsafe_epub_file = TEST_DIR / "william-shakespeare_richard-ii_with-script-tags.epub"
    assert not parse_epub(unsafe_epub_file)


def test_parse_azw3() -> None:
    """Test azw3 file."""
    safe_kindle_file = TEST_DIR / "laozi_tao-te-ching_james-legge.azw3"
    assert parse_kindle(safe_kindle_file)

    unsafe_kindle_file = (
        TEST_DIR / "laozi_tao-te-ching_james-legge_with-script-tags.azw3"
    )
    assert not parse_kindle(unsafe_kindle_file)


def test_parse_mobi() -> None:
    """Test mobi file."""
    # mobi files don't support JavaScript, so they are always safe (wrt script tags)

    safe_kindle_file: Path = TEST_DIR / "edith-wharton_ethan-frome.mobi"
    assert parse_kindle(safe_kindle_file)
