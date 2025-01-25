from typing import ClassVar, Self

import pymongo

from src.domain.__shared.value_objects import EmailAddress
from src.domain.__shared.value_objects.external_entity_id import ExternalEntityId
from src.domain.user import User
from src.infra.database.beanie.persistence_models.entity_pm import EntityPM


class UserPM(EntityPM):
    """The user persistence model."""

    username: str
    hashed_password: str
    email: str

    class Settings:  # noqa: D106
        name = "users"
        indexes: ClassVar[list] = [
            pymongo.IndexModel("username"),
            pymongo.IndexModel(
                "email",
                unique=True,
            ),
        ]

    def to_domain(self) -> User:
        """Converts the persistence model to the domain model."""
        return User(
            _id=self.id,
            external_id=ExternalEntityId(id=self.external_id),
            created_at=self.created_at,
            updated_at=self.updated_at,
            username=self.username,
            email=EmailAddress(self.email),
            hashed_password=self.hashed_password,
        )

    @classmethod
    def from_domain(cls, dm: User) -> Self:
        """Converts the domain model to the persistence model."""
        return cls(
            id=str(dm.id) if dm.id else None,
            external_id=str(dm.external_id),
            created_at=dm.created_at,
            updated_at=dm.updated_at,
            username=dm.username,
            email=dm.email.address,
            hashed_password=dm.hashed_password,
        )


__all__ = ["UserPM"]
