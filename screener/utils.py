"""
Screener utility functions.
"""

import logging

from bs4 import BeautifulSoup, ResultSet


def html_contains_javascript(content: bytes) -> bool:
    """Search for JavaScript in html files."""

    soup: BeautifulSoup = BeautifulSoup(content, "html.parser")
    scripts: ResultSet = soup.find_all("script")
    if scripts:
        logging.info("scripts detected: %s", scripts)
    return bool(scripts)
