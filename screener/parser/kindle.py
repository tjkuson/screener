from pathlib import Path

from screener.reader.kindle import KindleFileReader

from .epub import parse_epub


def parse_kindle(path_to_kindle: Path) -> bool:
    """Parse kindle to check that it is safe."""

    with KindleFileReader(path_to_kindle) as kindle:
        epub_translation: Path = Path(kindle.generated_epub)
        return parse_epub(epub_translation)
