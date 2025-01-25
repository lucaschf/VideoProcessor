from typing import Type

from pydantic import BaseModel

from src.domain.__shared.validator import IPydanticValidator
from src.domain.__shared.value_objects import EmailAddress


class UserValidationRule(BaseModel):
    username: str
    email: EmailAddress
    hashed_password: str


class UserValidator(IPydanticValidator):
    def get_pydantic_model(self) -> Type[BaseModel]:
        return UserValidationRule


class UserValidatorFactory:  # noqa: D101
    @staticmethod
    def create() -> UserValidator:  # noqa: D102
        return UserValidator()


__all__ = ["UserValidatorFactory"]
