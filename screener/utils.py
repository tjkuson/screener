"""Screener utility functions."""


from bs4 import BeautifulSoup

from screener.checker import Checker
from screener.diagnostic import ExternalImageDiagnostic, JavaScriptDiagnostic


def html_contains_javascript(
    checker: Checker, content: bytes
) -> list[JavaScriptDiagnostic] | None:
    """Check if HTML contains JavaScript."""
    soup = BeautifulSoup(content, "html.parser")
    if scripts := soup.find_all("script"):
        return [JavaScriptDiagnostic(checker.file_path.name, str(s)) for s in scripts]
    return None


def html_contains_images_with_external_sources(
    checker: Checker, content: bytes
) -> list[ExternalImageDiagnostic] | None:
    """Check if HTML contains images with external sources."""
    soup = BeautifulSoup(content, "html.parser")
    images = soup.find_all("img")
    if external_images := tuple(i for i in images if i["src"].startswith("http")):
        return [
            ExternalImageDiagnostic(checker.file_path.name, str(i))
            for i in external_images
        ]
    return None
