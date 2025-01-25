from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

from .value_object import ValueObject
from ..validator import ValidationResult, ValidationErrorDetails, DomainValidationError


@dataclass(kw_only=True, frozen=True, slots=True)
class InvalidExternalIdError(DomainValidationError):
    """Exception raised for invalid External Entity Ids."""

    external_entity_id: Optional[str]
    message: str = "ID inválido"


@dataclass(frozen=True, slots=True)
class ExternalEntityId(ValueObject):
    """Represents an external entity identifier.

    Attributes:
        id (str): The unique identifier for the external entity, defaulting to a new UUID.
    """

    id: str = field(default_factory=lambda: str(uuid4()))

    def _validate(self) -> ValidationResult:
        """Validates the UUID format of the id.

        Raises:
            InvalidExternalIdError: If the id is not a valid External ID.
        """
        if not isinstance(self.id, str):
            return ValidationResult(is_valid=False, errors=[
                ValidationErrorDetails(
                    loc=("id",),
                    msg="ID must be a string.",
                ),
            ])

        try:
            UUID(self.id)
        except (ValueError, TypeError):
            return ValidationResult(
                is_valid=False,
                errors=[
                    ValidationErrorDetails(
                        loc=("id",),
                        msg="ID must be a valid UUID.",
                    )
                ]
            )

        return ValidationResult(is_valid=True)

    def _build_exception(self, validation_result: ValidationResult) -> DomainValidationError:
        return InvalidExternalIdError(external_entity_id=self.id, errors=validation_result.errors)


__all__ = ["ExternalEntityId", "InvalidExternalIdError"]
