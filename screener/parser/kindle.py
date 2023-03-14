"""Parse kindle files."""

from pathlib import Path

from screener.reader.kindle import KindleFileReader

from .epub import parse_epub


def parse_kindle(path_to_kindle: Path | None) -> bool:
    """Parse kindle to check that it is safe."""
    if path_to_kindle is None:
        msg = "path_to_kindle cannot be None"
        raise ValueError(msg)
    with KindleFileReader(path_to_kindle) as kindle:
        if kindle.generated_translation is None:
            return False
        extension = Path(kindle.generated_translation).suffix
        match extension:
            case ".epub":
                epub_translation = Path(kindle.generated_translation)
                return parse_epub(epub_translation)

        # If failed to parse, assume it is not safe
        return False
