from abc import ABC
from datetime import datetime
from typing import TypeVar

from ..entity import Entity, entity
from ..validator import DomainValidationError, ValidationErrorDetails, ValidationResult
from ..value_objects import UniqueEntityId

T = TypeVar('T')


@entity
class AggregateRoot(Entity, ABC):
    """Base class for aggregate roots.

    Attributes:
        _id: The unique identifier for the aggregate root.
        created_at: The timestamp when the aggregate root was created.
        updated_at: The timestamp when the aggregate root was updated.
    """

    def _perform_validation(self) -> None:
        validation_result = self._validate()

        additional_validations = [
            self._validate_created_at(),
            self._validate_id(),
        ]

        for v in additional_validations:
            validation_result.errors.extend(v.errors)
            if not v.is_valid:
                validation_result.is_valid = False

        if not validation_result.is_valid:
            raise DomainValidationError(errors=validation_result.errors)

    def _validate_created_at(self) -> ValidationResult:
        """Validates the unique identifier.

        Returns:
            ValidationResult: The result of the validation operation.
        """
        if not isinstance(self.created_at, datetime):
            return ValidationResult(
                is_valid=False,
                errors=[
                    ValidationErrorDetails(
                        loc=("created_at",),
                        msg="The created_at field must be a datetime object.",
                    ),
                ],
            )
        return ValidationResult(is_valid=True)

    def _validate_id(self) -> ValidationResult:
        """Validates the unique identifier.

        Returns:
            ValidationResult: The result of the validation operation.
        """
        # If the id is not set, we assume that it is a new entity, and we don't need to validate it
        if not self.id or type(self.id) is UniqueEntityId:
            return ValidationResult(is_valid=True)

        return ValidationResult(
            is_valid=False,
            errors=[
                ValidationErrorDetails(
                    loc=("id",),
                    msg="The id field must be a UniqueEntityId object.",
                ),
            ],
        )


__all__ = ["AggregateRoot"]
