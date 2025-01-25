from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True, slots=True)
class ApplicationError(Exception):
    """Base class for application-level errors."""

    message: str


__all__ = [
    "ApplicationError",
]
