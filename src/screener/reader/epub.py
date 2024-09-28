from __future__ import annotations

import typing
import warnings

if typing.TYPE_CHECKING:
    from pathlib import Path
    from types import TracebackType

from ebooklib import epub


class EpubFileReader:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.book: epub.EpubBook

    def __enter__(self) -> EpubFileReader:
        with warnings.catch_warnings():
            # Have to do this because of bug in ebooklib.
            warnings.simplefilter("ignore")
            self.book = epub.read_epub(self.file_path, options={"ignore_ncx": False})
        return self

    @typing.overload
    def __exit__(self, exc_type: None, exc_val: None, exc_tb: None) -> None: ...

    @typing.overload
    def __exit__(
        self,
        exc_type: type[BaseException],
        exc_val: BaseException,
        exc_tb: TracebackType,
    ) -> None: ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
