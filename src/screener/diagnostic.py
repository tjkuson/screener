from dataclasses import dataclass


@dataclass
class Diagnostic:
    file_name: str
    # TODO(tom): report more diagnostic information.


@dataclass
class JavaScriptDiagnostic(Diagnostic):
    """Diagnostic information about a file with JavaScript."""

    culprit: str

    def __str__(self) -> str:
        return (
            f"JavaScript found in {self.file_name}: {self.culprit}"
            if self.culprit
            else f"JavaScript found in {self.file_name}"
        )


@dataclass
class ExternalImageDiagnostic(Diagnostic):
    """Diagnostic information about a file with external images."""

    culprit: str

    def __str__(self) -> str:
        return (
            f"External images found in {self.file_name}: {self.culprit}"
            if self.culprit
            else f"External images found in {self.file_name}"
        )


@dataclass
class ParseErrorDiagnostic(Diagnostic):
    """Diagnostic information about a file that could not be parsed."""

    msg: str
