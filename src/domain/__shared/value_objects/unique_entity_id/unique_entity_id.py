from dataclasses import dataclass

from ...validator import DomainValidationError, ValidationResult
from ..value_object import ValueObject, value_object
from .validator import UniqueEntityIdValidatorFactory


@dataclass(kw_only=True, frozen=True, slots=True)
class InvalidUniqueEntityIdError(DomainValidationError):
    """Exception raised for invalid Unique Entity Ids."""

    message: str = "ID inválido"
    entity_id: str


@value_object
class UniqueEntityId(ValueObject):
    """A Value Object that represents a unique entity identifier.

    It is used to uniquely identify entities in the domain model.
    """

    id: str

    def __post_init__(self) -> None:
        """Ensures the id is a string before initializing the UniqueEntityId."""
        super(UniqueEntityId, self).__post_init__()
        object.__setattr__(self, 'id', str(self.id))

    def _validate(self) -> ValidationResult:
        return UniqueEntityIdValidatorFactory.create().validate(self.id)

    def _build_exception(self, validation_result: ValidationResult) -> DomainValidationError:
        return InvalidUniqueEntityIdError(entity_id=self.id, errors=validation_result.errors)


__all__ = ["InvalidUniqueEntityIdError", "UniqueEntityId"]
