from injector import Module, inject, provider, singleton

from src.application.interfaces.password_hasher import IPasswordHasher
from src.application.use_cases.user.register.user_register_uc import RegisterUserUC
from src.domain.user.repository import IUserRepository
from src.infra.database.beanie.repositories.beanie_user_repository import BeanieUserRepository


class UserModule(Module):
    """Dependency injection module for the Role domain."""

    @singleton
    @provider
    def provide_user_repository(self) -> IUserRepository:
        """Provide the User repository."""
        return BeanieUserRepository()

    @provider
    @inject
    def provide_register_user_uc(
        self, user_repository: IUserRepository, password_hasher: IPasswordHasher
    ) -> RegisterUserUC:
        """Provide the user registration use case."""
        return RegisterUserUC(user_repo=user_repository, password_hasher=password_hasher)


__all__ = ["UserModule"]
