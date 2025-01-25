from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True, frozen=True, slots=True)
class InfrastructureError(Exception):
    """A custom exception class used to handle infrastructure-specific exceptions."""

    message: Optional[str] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={self.message!r})"

    def __str__(self) -> str:
        return repr(self)


@dataclass(kw_only=True, frozen=True, slots=True)
class StorageError(InfrastructureError):
    """Raised when an error occurs during a storage service call."""

    pass


@dataclass(kw_only=True, frozen=True, slots=True)
class EmailSenderError(InfrastructureError):
    """Raised when an error occurs during an email sender call."""

    message: str = "Falha no envio do email"


__all__ = ["EmailSenderError", "InfrastructureError", "StorageError"]
