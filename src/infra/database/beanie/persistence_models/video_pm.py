from typing import ClassVar, Self

import pymongo
from beanie import Link

from src.domain.__shared.value_objects.external_entity_id import ExternalEntityId
from src.domain.video import Video
from src.infra.database.beanie.persistence_models import UserPM
from src.infra.database.beanie.persistence_models.entity_pm import EntityPM


class VideoPM(EntityPM):
    """The video persistence model."""

    filename: str
    status: str
    processed_file: str | None
    user: Link[UserPM]

    class Settings:  # noqa: D106
        name = "videos"
        indexes: ClassVar[list] = [
            pymongo.IndexModel("filename", unique=True),
            pymongo.IndexModel("processed_file", unique=True),
        ]

    def to_domain(self) -> Video:
        """Converts the persistence model to the domain model."""
        return Video(
            _id=self.id,
            external_id=ExternalEntityId(id=self.external_),
            created_at=self.created_at,
            updated_at=self.updated_at,
            user=self.user.to_domain(),  # type: ignore
            filename=self.filename,
            status=self.status,
            processed_file=self.processed_file,
        )

    @classmethod
    def from_domain(cls, dm: Video) -> Self:
        """Converts the domain model to the persistence model."""
        return cls(
            id=str(dm.id) if dm.id else None,
            external_id=str(dm.external_id),
            created_at=dm.created_at,
            updated_at=dm.updated_at,
            user=UserPM.from_domain(dm=dm.user),
            filename=dm.filename,
            status=dm.status,
            processed_file=dm.processed_file,
        )


__all__ = ["VideoPM"]
