from bson import ObjectId

from src.domain.__shared.value_objects import EmailAddress, UniqueEntityId
from src.domain.user import User
from src.domain.user.repository import IUserRepository
from src.infra.database.beanie.persistence_models import UserPM


class BeanieUserRepository(IUserRepository):
    """Implementation of the UserRepository using Beanie."""

    async def insert(self, entity: User) -> User:
        """Insert a new user."""
        user_pm = await UserPM.from_domain(entity).insert()
        return user_pm.to_domain()

    async def find_by_id(self, identifier: str | UniqueEntityId) -> User | None:
        """Find a user by their ID."""
        user: UserPM | None = await UserPM.find_one(UserPM.id == ObjectId(str(identifier)))

        return user.to_domain() if user else None

    async def find_by_email(self, email: str | EmailAddress) -> User | None:
        """Find a user by email."""
        user: UserPM | None = await UserPM.find_one(UserPM.email == str(email))

        return user.to_domain() if user else None


__all__ = ["BeanieUserRepository"]
