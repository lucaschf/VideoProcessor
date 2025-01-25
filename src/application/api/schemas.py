from pydantic import BaseModel


class HttpErrorOut(BaseModel):
    """Basic error response model."""

    detail: str | None = None


common_error_responses = {
    400: {"model": HttpErrorOut},
    401: {"model": HttpErrorOut},
    403: {"model": HttpErrorOut},
}

common_error_responses_plus_not_found = {
    **common_error_responses,
    404: {"model": HttpErrorOut},
}

__all__ = ["HttpErrorOut", "common_error_responses", "common_error_responses_plus_not_found"]
