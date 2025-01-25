from abc import ABC, abstractmethod


class IFileStorage(ABC):
    @abstractmethod
    def upload_file(self, file_name: str, file_data: bytes) -> None:
        """Uploads a file to storage."""
        pass

    @abstractmethod
    def download_file(self, file_name: str) -> bytes:
        """Downloads a file from storage."""
        pass


__all__ = ['IFileStorage']
