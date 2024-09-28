from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from types import TracebackType


class AbstractReader:
    def __init__(self: AbstractReader, file_path: Path) -> None:
        self.file_path = file_path

    def __enter__(self: AbstractReader) -> AbstractReader:
        raise NotImplementedError

    def __exit__(
        self: AbstractReader,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
