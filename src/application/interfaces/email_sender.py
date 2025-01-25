from abc import ABC, abstractmethod
from typing import List

from src.domain.__shared.value_objects.email.email import Email


class IEmailSender(ABC):
    @abstractmethod
    def send_email(self, email: Email) -> None:
        """Sends an email."""
        pass

    @abstractmethod
    def send_bulk_emails(self, emails: List[Email]) -> None:
        """Sends multiple emails."""
        pass


__all__ = ["IEmailSender"]
