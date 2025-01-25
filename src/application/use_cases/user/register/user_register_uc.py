from src.application.error import EmailAlreadyRegisteredError, InvalidPasswordError
from src.application.interfaces.password_hasher import IPasswordHasher
from src.application.use_cases.user.register.dto import UserRegisteredDTO, UserRegistrationDTO
from src.domain.__shared.value_objects import EmailAddress
from src.domain.user import User
from src.domain.user.repository import IUserRepository


class RegisterUserUC:
    """Use-case for registering a new user."""

    def __init__(self, user_repo: IUserRepository, password_hasher: IPasswordHasher) -> None:
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def register(self, user_data: UserRegistrationDTO) -> UserRegisteredDTO:
        """Validates and register a new user."""
        user = await self.user_repo.find_by_email(user_data.email)

        if user:
            raise EmailAlreadyRegisteredError(email=user_data.email)

        if len(user_data.email) < 3:
            raise InvalidPasswordError()

        hashed_password = self.password_hasher.hash(user_data.password)

        user = User(
            username=user_data.username,
            email=EmailAddress(address=user_data.email),
            hashed_password=hashed_password,
        )
        created_user = await self.user_repo.insert(user)
        return UserRegisteredDTO(id=str(created_user.external_id))


__all__ = ["RegisterUserUC"]
