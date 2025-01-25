from abc import ABC, abstractmethod


class IPasswordHasher(ABC):
    """Interface for password hashing services."""

    @abstractmethod
    def hash(self, password: str) -> str:
        """Hashes a password.

        Args:
            password (str): The plain text password to be hashed.

        Returns:
            str: The hashed password.
        """
        pass

    @abstractmethod
    def verify(self, password: str, hashed_password: str) -> bool:
        """Verifies a password against a hashed password.

        Args:
            password: The plain text password to verify.
            hashed_password: The hashed password to verify against.

        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        pass


__all__ = ["IPasswordHasher"]
