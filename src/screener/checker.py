from dataclasses import dataclass, field
from pathlib import Path

from screener.diagnostic import Diagnostic


@dataclass
class Checker:
    file_path: Path
    diagnostics: list[Diagnostic] = field(default_factory=list)
