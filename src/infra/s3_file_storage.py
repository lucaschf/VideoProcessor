import io

import boto3
from botocore.exceptions import BotoCoreError, ClientError

from src.application.interfaces import IFileStorage
from src.infra.error import StorageError


class S3FileStorage(IFileStorage):
    def __init__(
        self,
        bucket_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        region_name: str = 'us-east-1'
    ):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def upload_file(self, file_name: str, file_data: bytes) -> None:
        try:
            self.s3_client.put_object(file_data, self.bucket_name, file_name)
        except (BotoCoreError, ClientError) as e:
            raise StorageError(message='Falha no envio do arquivo') from e

    def download_file(self, file_name: str) -> bytes:
        try:
            file_obj = io.BytesIO()
            self.s3_client.download_fileobj(self.bucket_name, file_name, file_obj)
            file_obj.seek(0)
            return file_obj.read()
        except (BotoCoreError, ClientError) as e:
            raise StorageError(message="Falha no download do arquivo") from e


__all__ = ['S3FileStorage']
