from dataclasses import dataclass


@dataclass
class Diagnostic:
    file_name: str


@dataclass
class JavaScriptDiagnostic(Diagnostic):
    culprit: str

    def __str__(self) -> str:
        return (
            f"JavaScript found in {self.file_name}: {self.culprit}"
            if self.culprit
            else f"JavaScript found in {self.file_name}"
        )


@dataclass
class ExternalImageDiagnostic(Diagnostic):
    culprit: str

    def __str__(self) -> str:
        return (
            f"External images found in {self.file_name}: {self.culprit}"
            if self.culprit
            else f"External images found in {self.file_name}"
        )


@dataclass
class ParseErrorDiagnostic(Diagnostic):
    msg: str
