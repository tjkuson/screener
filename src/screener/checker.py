"""Checker class for checking the data."""
from dataclasses import dataclass, field
from pathlib import Path

from screener.diagnostic import Diagnostic


@dataclass
class Checker:
    """Checker class for checking the data."""

    file_path: Path
    diagnostics: list[Diagnostic] = field(default_factory=list)
