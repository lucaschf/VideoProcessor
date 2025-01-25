from typing import List

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from src.application.interfaces.email_sender import IEmailSender
from src.domain.__shared.value_objects.email.email import Email
from src.infra.error import EmailSenderError


class SESEmailSender(IEmailSender):
    """Implements the IEmailSender interface using Amazon SES."""

    def __init__(
        self, aws_access_key_id: str, aws_secret_access_key: str, region_name: str = "us-east-1"
    ) -> None:
        self.region_name = region_name
        try:
            self.ses_client = boto3.client(
                "ses",
                region_name=self.region_name,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
            )
        except (BotoCoreError, ClientError) as e:
            raise EmailSenderError(message=f"Failed to initialize SES client: {e}") from e

    def send_email(self, email: Email) -> None:
        """Sends a single email using Amazon SES.

        Arguments:
            email: An instance of Email containing email details.

        Raises:
            EmailSenderError: If sending the email via SES fails.
        """
        try:
            self.ses_client.send_email(
                Source=email.from_address,
                Destination={"ToAddresses": email.to_addresses},
                Message={
                    "Subject": {"Data": email.subject, "Charset": "UTF-8"},
                    "Body": {"Text": {"Data": email.body, "Charset": "UTF-8"}},
                },
            )
        except (BotoCoreError, ClientError) as e:
            raise EmailSenderError(message="Failed to send email") from e

    def send_bulk_emails(self, emails: List[Email]) -> None:
        """Sends multiple emails using Amazon SES.

        Arguments:
            emails: A list of Email instances containing email details.

        Raises:
             EmailSenderError: If sending any of the emails via SES fails.
        """
        try:
            for email in emails:
                self.send_email(email)
        except Exception as e:
            raise EmailSenderError(message="Failed to send bulk emails") from e


__all__ = ["SESEmailSender"]
