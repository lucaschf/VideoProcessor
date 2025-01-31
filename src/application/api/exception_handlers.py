from http import HTTPStatus

from fastapi import Request
from starlette.responses import JSONResponse, Response

from src.application.error import ApplicationError
from src.domain.__shared.error import DomainError
from src.domain.__shared.validator import DomainValidationError
from src.infra.error import InfrastructureError


def domain_validation_exception_handler(_request: Request, exc: Exception) -> Response:
    """Handles DomainValidationError exceptions.

    This handler specifically addresses `DomainValidationError` exceptions,
    which typically occur during data validation. It formats the error details
    into a JSON response with a 422 Unprocessable Entity status code, maintaining
    compatibility with FastAPI's default error response structure.

    Args:
        _request: The incoming FastAPI request object (unused in this handler).
        exc: The exception object, expected to be a `DomainValidationError`.

    Returns:
        A JSON response containing the formatted error details.

    Raises:
        exc: Re-raises any other exception type for further handling.
    """
    if isinstance(exc, DomainValidationError):
        error_type = "value_error"
        return JSONResponse(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            content={
                "detail": [
                    {
                        "loc": e.loc,
                        "msg": e.msg,
                        "type": error_type,
                    }
                    for e in exc.errors
                ],
            },
        )

    raise exc


def domain_exception_handler(_request: Request, exc: Exception) -> Response:
    """Handles DomainError exceptions.

    This handler is designed to manage `DomainError` exceptions, which
    represent errors specific to the application's domain logic. It generates
    a JSON response with a 400 Bad Request status code and the error message.

    Args:
        _request: The incoming FastAPI request object (unused in this handler).
        exc: The exception object, expected to be a `DomainError`.

    Returns:
        A JSON response containing the error message.

    Raises:
        exc: Re-raises any other exception type for further handling.
    """
    if isinstance(exc, DomainError):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"detail": exc.message},
        )

    raise exc


def application_exception_handler(_request: Request, exc: Exception) -> Response:
    """Handles ApplicationError exceptions.

    This handler is designed to manage `ApplicationError` exceptions, which
    represent errors specific to the application's domain logic.
    It generates a JSON response with a 400 Bad Request status code and the error message.

    Args:
        _request: The incoming FastAPI request object (unused in this handler).
        exc: The exception object, expected to be a `ApplicationError`.

    Returns:
        A JSON response containing the error message.

    Raises:
        exc: Re-raises any other exception type for further handling.
    """
    if isinstance(exc, ApplicationError):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={"detail": exc.message},
        )

    raise exc


def infrastructure_exception_handler(_request: Request, exc: Exception) -> Response:
    """Handles general exceptions.

    This handler acts as a catch-all for any unhandled exceptions. It prints
    the exception traceback for debugging purposes and returns a JSON response
    with a 500 Internal Server Error status code.

    Args:
        _request: The incoming FastAPI request object (unused in this handler).
        exc: The exception object.

    Returns:
        A JSON response indicating an internal server error.
    """
    if isinstance(exc, InfrastructureError):
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "detail": (
                    "Ocorreu um erro ao processar sua solicitação."
                    " Por favor, tente novamente mais tarde."
                ),
            },
        )

    raise exc


def general_exception_handler(_request: Request, _exc: Exception) -> Response:
    """Handles general exceptions.

    This handler acts as a catch-all for any unhandled exceptions. It prints
    the exception traceback for debugging purposes and returns a JSON response
    with a 500 Internal Server Error status code.

    Args:
        _request: The incoming FastAPI request object (unused in this handler).
        _exc: The exception object.

    Returns:
        A JSON response indicating an internal server error.
    """
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={
            "detail": (
                "Ocorreu um erro ao processar sua solicitação."
                " Por favor, tente novamente mais tarde."
            ),
        },
    )


__all__ = [
    "application_exception_handler",
    "domain_exception_handler",
    "domain_validation_exception_handler",
    "general_exception_handler",
    "infrastructure_exception_handler",
]
