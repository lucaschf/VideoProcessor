from dataclasses import dataclass

from src.domain.__shared.entity import Entity
from src.domain.__shared.validator import ValidationResult
from src.domain.user import User
from src.domain.video.video_entity_validator import VideoValidatorFactory


@dataclass(kw_only=True, slots=True)
class Video(Entity):
    """A class representing a video entity."""

    user: User
    filename: str
    status: str
    processed_file: str | None

    def _validate(self) -> ValidationResult:
        return VideoValidatorFactory.create().validate(self)


__all__ = ["Video"]
