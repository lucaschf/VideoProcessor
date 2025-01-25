from pydantic import BaseModel, EmailStr, Field

from src.application.api.types import PydanticExternalEntityId
from src.application.use_cases.user.register.dto import UserRegistrationDTO


class UserRegistrationIN(BaseModel):
    """Input data for user registration."""

    username: str = Field(min_length=3)
    email: EmailStr
    password: str = Field(min_length=3)

    def to_dto(self) -> UserRegistrationDTO:
        """Convert Pydantic model to DTO."""
        return UserRegistrationDTO(
            username=self.username,
            email=str(self.email),
            password=self.password,
        )


class UserRegistrationOUT(BaseModel):
    """Output data for user registration."""

    id: PydanticExternalEntityId


__all__ = ["UserRegistrationIN", "UserRegistrationOUT"]
