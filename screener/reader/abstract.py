from pathlib import Path


class AbstractReader:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
