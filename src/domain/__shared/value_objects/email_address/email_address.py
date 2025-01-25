from dataclasses import dataclass
from typing import Optional

from ...validator import DomainValidationError, ValidationResult
from ..value_object import ValueObject, value_object
from .validator import EmailAddressValidatorFactory


@dataclass(frozen=True, kw_only=True, slots=True)
class InvalidEmailAddressError(DomainValidationError):
    """Exception raised when an email is invalid."""

    address: Optional[str]
    message: str = "Endereço de e-mail inválido."


@value_object
class EmailAddress(ValueObject):
    """A Value Object that represents an Email.

    This class validates the email using a simple regular expression.
    """

    address: str

    def _validate(self) -> ValidationResult:
        return EmailAddressValidatorFactory.create().validate(self)

    def _build_exception(self, validation_result: ValidationResult) -> DomainValidationError:
        return InvalidEmailAddressError(address=self.address, errors=validation_result.errors)


__all__ = ["EmailAddress", "InvalidEmailAddressError"]
