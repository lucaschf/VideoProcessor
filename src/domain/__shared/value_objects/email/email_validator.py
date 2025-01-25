from typing import Type

from pydantic import BaseModel, Field

from src.domain.__shared.validator import IPydanticValidator, IValidator
from src.domain.__shared.value_objects import EmailAddress


class EmailValidationRule(BaseModel):
    """A Pydantic model that represents a validation rule for an Email value object.

    This class is responsible for defining the rules that will be used to
    validate an email.
    """

    subject: str
    body: str
    to_addresses: list[EmailAddress] = Field(min_length=1)
    from_address: EmailAddress


class EmailValidator(IPydanticValidator):
    """A validator for Email value objects."""

    def get_pydantic_model(self) -> Type[BaseModel]:
        """Gets the Pydantic model used for validation."""
        return EmailValidationRule


class EmailValidatorFactory:
    """A factory class for creating instances of EmailValidator."""

    @staticmethod
    def create() -> IValidator:
        """Creates a new instance of EmailValidator."""
        return EmailValidator()


__all__ = ["EmailValidatorFactory"]
