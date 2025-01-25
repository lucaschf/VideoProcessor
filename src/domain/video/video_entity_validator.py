from typing import Type

from pydantic import BaseModel

from src.domain.__shared.validator import IPydanticValidator
from src.domain.user import User


class VideoValidationRule(BaseModel):
    user: User
    filename: str
    status: str
    processed_file: str | None


class VideoValidator(IPydanticValidator):
    def get_pydantic_model(self) -> Type[VideoValidationRule]:
        return VideoValidationRule


class VideoValidatorFactory:  # noqa: D101
    @staticmethod
    def create() -> VideoValidator:  # noqa: D102
        return VideoValidator()


__all__ = ["VideoValidatorFactory"]
