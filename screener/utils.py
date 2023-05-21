"""Screener utility functions."""

import logging

from bs4 import BeautifulSoup


def html_contains_javascript(content: bytes) -> bool:
    """Search for JavaScript in html files."""
    soup = BeautifulSoup(content, "html.parser")
    scripts = soup.find_all("script")
    if scripts:
        logging.info("scripts detected: %s", scripts)
    return bool(scripts)


def html_contains_images_with_external_sources(content: bytes) -> bool:
    """Search for images with external sources in html files."""
    soup = BeautifulSoup(content, "html.parser")
    images = soup.find_all("img")
    return any(i for i in images if i["src"].startswith("http"))
