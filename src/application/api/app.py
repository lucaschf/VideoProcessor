from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.application.error import ApplicationError
from src.config.settings import settings
from src.domain.__shared.error import DomainError
from src.domain.__shared.validator import DomainValidationError
from src.infra.database.beanie import initialize_database

from ...infra.error import InfrastructureError
from .exception_handlers import (
    application_exception_handler,
    domain_exception_handler,
    domain_validation_exception_handler,
    general_exception_handler,
    infrastructure_exception_handler,
)
from .middlewares import setup_cors
from .routers import register_routes


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:  # noqa: RUF029, ARG001
    """Lifespan context manager for FastAPI application.

    This function defines the startup and shutdown logic for the FastAPI application.
    It connects to the database before the application starts receiving requests,
    and disconnects from the database after the application has finished handling requests.

    This ensures that the database connection is available for the
    entire lifespan of the application, and is properly cleaned up afterward.

    Args:
        _app (FastAPI): The FastAPI application instance.

    Yields:
        None: This context manager does not return any value.

    For more details, refer to the FastAPI documentation on Lifespan Events:
    https://fastapi.tiangolo.com/advanced/events/#lifespan-events
    """
    async with initialize_database(
        settings.DB_URI,
        settings.DB_NAME,
    ):
        yield


app = FastAPI(
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    title=f"{settings.PROJECT_NAME}",
    lifespan=lifespan,
)

register_routes(app)
setup_cors(app, ["*"])  # allow all origins for now

app.add_exception_handler(DomainValidationError, domain_validation_exception_handler)
app.add_exception_handler(ApplicationError, application_exception_handler)
app.add_exception_handler(DomainError, domain_exception_handler)
app.add_exception_handler(InfrastructureError, infrastructure_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

__all__ = ["app"]
