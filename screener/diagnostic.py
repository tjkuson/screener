"""Diagnostic information about a file."""
from dataclasses import dataclass


@dataclass
class Diagnostic:
    """Diagnostic information about a file."""

    file_name: str


@dataclass
class JavaScriptDiagnostic(Diagnostic):
    """Diagnostic information about a file with JavaScript."""


@dataclass
class ExternalImageDiagnostic(Diagnostic):
    """Diagnostic information about a file with external images."""


@dataclass
class ParseErrorDiagnostic(Diagnostic):
    """Diagnostic information about a file that could not be parsed."""

    msg: str
