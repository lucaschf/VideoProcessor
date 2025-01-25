from dataclasses import dataclass

from src.domain.__shared.validator import ValidationResult
from src.domain.__shared.value_objects import EmailAddress, ValueObject
from src.domain.__shared.value_objects.email.email_validator import EmailValidatorFactory


@dataclass(frozen=True, kw_only=True, slots=True)
class Email(ValueObject):
    """Represents an email message with the subject, body, recipient, and sender."""

    subject: str
    body: str
    to_addresses: list[EmailAddress]
    from_address: EmailAddress

    def _validate(self) -> ValidationResult:
        return EmailValidatorFactory.create().validate(self)


__all__ = ["Email"]
