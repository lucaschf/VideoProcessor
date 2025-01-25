"""Database.

This module configures and manages the connection to the MongoDB database and contains
the Beanie data models that represent the MongoDB collection documents.
Beanie models provide ORM functionality to simplify CRUD operations with the database.
"""

from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Mapping

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .persistence_models import UserPM, VideoPM

database_models = [VideoPM, UserPM]


@asynccontextmanager
async def initialize_database(
    db_uri: str,
    db_name: str,
) -> AsyncGenerator[AsyncIOMotorClient[Mapping[str, Any] | Any], Any]:
    """Initialize the connection with MongoDB and Beanie for document models.

    This function performs the following actions:

    Establishes an asynchronous connection with MongoDB
     using the URI provided in the settings.
    Select the specified database from the settings.
    Initializes Beanie for the specified document models.
    This step is crucial for Beanie to operate correctly with MongoDB.

    Raises:
            ConnectionError: If the connection to MongoDB fails.
            RuntimeError: If the Beanie initialization fails or document models are not specified.
    """
    client = AsyncIOMotorClient(db_uri)
    database = client[db_name]

    # Beanie initialization
    await init_beanie(database, document_models=database_models)
    yield client

    client.close()


__all__ = ["initialize_database"]
