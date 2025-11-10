from pydantic import BaseModel, Field

from src.core.infra.enums import ErrorStatus


class BaseApiResponse(BaseModel):
    """
    Standard structure for successful API responses.

    Attributes:
        status (str): Response status, typically "ok" for success or "error" for failure.
        message (str): Human-readable message describing the response.
    """
    status: str = Field(default="ok", examples=["ok", "error"])
    message: str


class ErrorData(BaseModel):
    """
    Structured data representing an API error.

    Attributes:
        code (int): HTTP status code of the error.
        message (str): Human-readable error message.
        status (ErrorStatus): Machine-readable error status from ErrorStatus enum.
    """
    code: int
    message: str
    status: ErrorStatus


class ErrorResponse(BaseModel):
    """
    Wrapper for API error responses.

    Attributes:
        error (ErrorData): The error details contained in the response.
    """
    error: ErrorData
