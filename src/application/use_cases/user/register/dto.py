from dataclasses import dataclass


@dataclass(kw_only=True, slots=True, frozen=True)
class UserRegistrationDTO:
    """Input data for registration."""

    username: str
    email: str
    password: str


@dataclass(kw_only=True, slots=True, frozen=True)
class UserRegisteredDTO:
    """Result of user registration."""

    id: str


__all__ = ["UserRegisteredDTO", "UserRegistrationDTO"]
