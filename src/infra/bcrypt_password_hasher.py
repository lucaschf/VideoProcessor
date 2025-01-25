import bcrypt

from src.application.interfaces.password_hasher import IPasswordHasher


class BcryptPasswordHasher(IPasswordHasher):
    """Implementation of IPasswordHasher using bcrypt."""

    def hash(self, password: str) -> str:
        """Hash a password using bcrypt."""
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    def verify(self, password: str, hashed_password: str) -> bool:
        """Verify a password against a hashed password."""
        if not isinstance(hashed_password, str):
            return False

        try:
            hashed_bytes = hashed_password.encode("utf-8")  # ou 'ascii'
            return bcrypt.checkpw(password.encode("utf-8"), hashed_bytes)
        except (ValueError, TypeError):
            return False


__all__ = ["BcryptPasswordHasher"]
