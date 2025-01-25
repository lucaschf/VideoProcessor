import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, fields
from typing import TypeVar

from src.domain.__shared.validator import DomainValidationError, ValidationResult

T = TypeVar('T')


value_object = dataclass(frozen=True, kw_only=True, slots=True)
"""A decorator to define a Value Object class.

It will have the following characteristics:

- The class is frozen (immutable).
- Only keyword arguments are allowed in the constructor.
- The class uses slots to optimize memory usage.

Args:
    cls (Type): The class to be decorated.

Returns:
    Type: The decorated class with the specified properties.
"""


@value_object
class ValueObject(ABC):
    """Base class for Value Objects, enforcing validation upon initialization.

    Subclasses must implement:
      - _validate() -> ValidationResult
    """

    def __post_init__(self) -> None:
        """Performs validation after the object is initialized."""
        self._perform_validation()

    def _perform_validation(self) -> None:
        """Perform validation with the _validate method.

        Raises:
            DomainValidationError: If the validation fails.
        """
        validation_result = self._validate()
        if not validation_result.is_valid:
            raise self._build_exception(validation_result)

    @abstractmethod
    def _validate(self) -> ValidationResult:
        """Validates the Value Object.

        Returns:
            ValidationResult: Result of the validation.
        """
        pass

    def _build_exception(self, validation_result: ValidationResult) -> DomainValidationError:
        """Builds an exception based on the validation result.

        Args:
            validation_result (ValidationResult): The result of the validation.

        Returns:
            DomainValidationError: The exception to be raised.
        """
        return DomainValidationError(errors=validation_result.errors)

    def __str__(self) -> str:
        """Returns a JSON-formatted string of all fields in this Value Object.

        - Uses ``json.dumps`` with ``default=str`` to gracefully handle
          any non-serializable field by converting it to a string.
        """
        field_values = {f.name: getattr(self, f.name) for f in fields(self)}
        if len(field_values) > 1:
            return json.dumps(field_values, default=str)
        return str(next(iter(field_values.values())))


__all__ = ['ValueObject', 'value_object']
