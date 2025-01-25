from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, TypeVar

from ..validator import DomainValidationError, ValidationResult
from ..value_objects import UniqueEntityId
from ..value_objects.external_entity_id import ExternalEntityId

T = TypeVar('T')


entity = dataclass(kw_only=True, slots=True)
"""A decorator to define an Entity class.

It will have the following characteristics:

- Only keyword arguments are allowed in the constructor.
- The class uses slots to optimize memory usage.

Args:
    cls (Type): The class to be decorated.

Returns:
    Type: The decorated class with the specified properties.
"""


@dataclass(kw_only=True, slots=True)
class Entity(ABC):
    """Base class for all entities (non-aggregate roots)."""
    _id: Optional[UniqueEntityId] = None
    external_id: ExternalEntityId = field(default_factory=ExternalEntityId)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @property
    def id(self) -> Optional[UniqueEntityId]:
        return self._id

    def __post_init__(self) -> None:
        self._perform_validation()

    def _perform_validation(self) -> None:
        validation_result = self._validate()
        if not validation_result.is_valid:
            raise DomainValidationError(errors=validation_result.errors)

    @abstractmethod
    def _validate(self) -> ValidationResult:
        """Subclasses must implement validation of their own state and return a ValidationResult."""


__all__ = ['Entity', 'entity']
