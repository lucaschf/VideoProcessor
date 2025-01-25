from datetime import datetime
from typing import ClassVar

import pymongo
from beanie import Document


class EntityPM(Document):
    """A base persistence model for domain Entities that leverages Beanie (Document)."""

    external_id: str
    created_at: datetime
    updated_at: datetime

    class Settings:  # noqa: D106
        indexes: ClassVar[list] = [
            pymongo.IndexModel("external_entity_id", unique=True),
        ]


__all__ = ["EntityPM"]
