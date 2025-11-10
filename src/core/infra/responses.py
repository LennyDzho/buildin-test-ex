from fastapi.responses import JSONResponse

from src.core.infra.enums import ErrorStatus
from src.core.infra.schemas import ErrorResponse, ErrorData


class ErrorJsonResponse(JSONResponse):
    """
    Custom JSON response for standardized API error messages.

    Constructs a JSON response containing structured error information,
    including HTTP status code, error message, and a defined error status.

    Args:
        code (int): HTTP status code for the response.
        message (str): Human-readable error message.
        status (ErrorStatus): Machine-readable error status from ErrorStatus enum.

    Example:
        ErrorJsonResponse(
            code=404,
            message="Resource not found",
            status=ErrorStatus.NOT_FOUND
        )
    """

    def __init__(
        self,
        *,
        code: int,
        message: str,
        status: ErrorStatus,
    ):
        error_data = ErrorData(code=code, message=message, status=status)
        super().__init__(
            status_code=code,
            content=ErrorResponse(error=error_data).model_dump(),
            media_type="application/json; charset=utf-8",
        )
