from __future__ import annotations

import shutil
import typing

if typing.TYPE_CHECKING:
    from pathlib import Path
    from types import TracebackType

from mobi import extract


class KindleFileReader:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self._temp_dir = None
        self.generated_translation = None

    def __enter__(self) -> KindleFileReader:
        # The `mobi` library likes file paths as strings for whatever reason.
        self._temp_dir, self.generated_translation = extract(str(self.file_path))
        if self.generated_translation is None or self._temp_dir is None:
            msg = "Could not extract Kindle file"
            raise ValueError(msg)
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
    ) -> None:
        if self._temp_dir is not None:
            shutil.rmtree(self._temp_dir)
