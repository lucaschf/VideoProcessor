from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from src.domain.__shared.entity import Entity
from src.domain.__shared.value_objects import UniqueEntityId

T = TypeVar("T", bound=Entity)


class IRepository(ABC, Generic[T]):
    """Interface for a generic repository.

    This interface defines the basic CRUD operations for a repository.
    """

    @abstractmethod
    async def insert(self, entity: T) -> T:
        """Create a new entity in the repository.

        Args:
            entity (T): The entity to be created.

        Returns:
            T: The created entity.

        Raises:
            DuplicatedKeyRepositoryError: If the entity already exists in the repository.
        """
        pass

    @abstractmethod
    async def find_by_id(self, identifier: str | UniqueEntityId) -> T | None:
        """Find an entity by its identifier.

        Args:
            identifier (str | UniqueEntityId): The identifier of the entity.

        Returns:
            T | None: The found entity or None if not found.
        """
        pass


__all__ = ["IRepository"]
