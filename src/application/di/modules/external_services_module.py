from injector import Module, provider, singleton

from src.application.interfaces import IFileStorage
from src.application.interfaces.email_sender import IEmailSender
from src.application.interfaces.password_hasher import IPasswordHasher
from src.config.settings import settings
from src.infra.bcrypt_password_hasher import BcryptPasswordHasher
from src.infra.s3_file_storage import S3FileStorage
from src.infra.ses_email_sender import SESEmailSender


class ExternalServiceModule(Module):
    """Dependency injection module for external services."""

    @singleton
    @provider
    def provide_file_storage_service(self) -> IFileStorage:
        """Provide the file storage service."""
        return S3FileStorage(
            bucket_name=settings.S3_BUCKET_NAME,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )

    @singleton
    @provider
    def provide_email_sender_service(self) -> IEmailSender:
        """Provide the email sender service."""
        return SESEmailSender(
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_REGION,
        )

    @singleton
    @provider
    def provide_password_hasher(self) -> IPasswordHasher:
        """Provide a password hasher."""
        return BcryptPasswordHasher()


__all__ = ["ExternalServiceModule"]
