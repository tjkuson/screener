"""Parse kindle files."""

from pathlib import Path

from screener.checker import Checker
from screener.reader.kindle import KindleFileReader

from .epub import parse_epub


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
            msg = "generated_translation cannot be None"
            raise FileNotFoundError(msg)
        extension = Path(kindle.generated_translation).suffix
        match extension:
            case ".epub":
                epub_translation = Path(kindle.generated_translation)
                parse_epub(checker, epub_translation)
                return
