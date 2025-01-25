from dataclasses import dataclass

from src.domain.__shared.entity import Entity
from src.domain.__shared.validator import ValidationResult
from src.domain.__shared.value_objects import EmailAddress
from src.domain.user.user_entity_validator import UserValidatorFactory


@dataclass(kw_only=True, slots=True)
class User(Entity):
    """A class representing a user entity."""

    username: str
    email: EmailAddress
    hashed_password: str

    def _validate(self) -> ValidationResult:
        return UserValidatorFactory.create().validate(self)


__all__ = ["User"]
