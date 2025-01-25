from abc import ABC, abstractmethod

from src.domain.__shared.interfaces import IRepository
from src.domain.__shared.value_objects import EmailAddress
from src.domain.user import User


class IUserRepository(IRepository[User], ABC):
    """Repository for the user Entity."""

    @abstractmethod
    async def find_by_email(self, email: str | EmailAddress) -> User | None:
        """Finds a user by their email address."""
        pass


__all__ = ["IUserRepository"]
