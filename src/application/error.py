from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True, slots=True)
class ApplicationError(Exception):
    """Base class for application-level errors."""

    message: str


@dataclass(kw_only=True, frozen=True, slots=True)
class EmailAlreadyRegisteredError(ApplicationError):
    """Exception raised when a user with the same email already exists."""

    message: str = "Ja existe um usuario com o email informado"
    email: str


@dataclass(kw_only=True, frozen=True, slots=True)
class InvalidPasswordError(ApplicationError):
    """Exception raised when a password is invalid."""

    message: str = "Senha invalida"


__all__ = ["ApplicationError", "EmailAlreadyRegisteredError"]
