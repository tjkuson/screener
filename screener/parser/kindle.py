"""Parse kindle files."""

from pathlib import Path

from screener.diagnostic import (
    ExternalImageDiagnostic,
    JavaScriptDiagnostic,
    ParseErrorDiagnostic,
)
from screener.reader.kindle import KindleFileReader

from .epub import parse_epub


def parse_kindle(
    path_to_kindle: Path | None,
) -> JavaScriptDiagnostic | ExternalImageDiagnostic | ParseErrorDiagnostic | None:
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
                if (diagnostic := parse_epub(epub_translation)) is not None:
                    diagnostic.file_name = path_to_kindle.name
                    return diagnostic
                return None

        # If failed to parse, assume it is unsafe.
        return ParseErrorDiagnostic(path_to_kindle.name, "could not process file")
