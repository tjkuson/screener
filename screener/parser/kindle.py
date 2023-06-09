"""Parse kindle files."""

from pathlib import Path

from screener.diagnostic import (
    ExternalImageDiagnostic,
    JavaScriptDiagnostic,
    ParseErrorDiagnostic,
)
from screener.reader.kindle import KindleFileReader

from .epub import parse_epub
from ..checker import Checker


def parse_kindle(
    checker: Checker,
    path_to_kindle: Path | None,
) -> None:
    """Parse kindle to check that it is safe."""
    if path_to_kindle is None:
        msg = "path_to_kindle cannot be None"
        raise ValueError(msg)
    with KindleFileReader(path_to_kindle) as kindle:
        if kindle.generated_translation is None:
            return ParseErrorDiagnostic(
                path_to_kindle.name, "failed to generate translation"
            )
        extension = Path(kindle.generated_translation).suffix
        match extension:
            case ".epub":
                epub_translation = Path(kindle.generated_translation)
                parse_epub(checker, epub_translation)
