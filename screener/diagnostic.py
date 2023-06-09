"""Diagnostic information about a file."""
from dataclasses import dataclass


@dataclass
class Diagnostic:
    """Diagnostic information about a file."""

    file_name: str


@dataclass
class JavaScriptDiagnostic(Diagnostic):
    """Diagnostic information about a file with JavaScript."""

    def __str__(self) -> str:
        """Return a string representation of the diagnostic."""
        return f"JavaScript found in {self.file_name}"


@dataclass
class ExternalImageDiagnostic(Diagnostic):
    """Diagnostic information about a file with external images."""

    def __str__(self) -> str:
        """Return a string representation of the diagnostic."""
        return f"External images found in {self.file_name}"


@dataclass
class ParseErrorDiagnostic(Diagnostic):
    """Diagnostic information about a file that could not be parsed."""

    msg: str
