"""Parse kindle files."""

from pathlib import Path

from screener.reader.kindle import KindleFileReader

from .epub import parse_epub


def parse_kindle(path_to_kindle: Path) -> bool:
    """Parse kindle to check that it is safe."""
    with KindleFileReader(path_to_kindle) as kindle:
        extension: str = Path(kindle.generated_translation).suffix
        match extension:
            case ".epub":
                epub_translation: Path = Path(kindle.generated_translation)
                return parse_epub(epub_translation)

        # If failed to parse, assume it is not safe
        return False
