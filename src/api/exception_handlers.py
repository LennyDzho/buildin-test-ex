import logging
from fastapi import Request, status, Response

from src.core.infra import ErrorJsonResponse, ErrorStatus


logger = logging.getLogger(__name__)


async def not_api_key_exception_handler(_request: Request, _exc: Exception) -> Response:
    """
    Handle the case when an API key is missing from the request.

    Returns a 401 Unauthorized JSON response with a descriptive error message.

    Args:
        _request (Request): The incoming FastAPI request (unused).
        _exc (Exception): The raised exception instance (unused).

    Returns:
        Response: A JSON-formatted error response indicating the missing API key.
    """
    return ErrorJsonResponse(
        code=status.HTTP_401_UNAUTHORIZED,
        message="API key not found",
        status=ErrorStatus.UNAUTHENTICATED,
    )


async def invalid_api_key_exception_handler(
    _request: Request, _exc: Exception
) -> Response:
    """
    Handle the case when an invalid API key is provided.

    Returns a 403 Forbidden JSON response with an appropriate error message.

    Args:
        _request (Request): The incoming FastAPI request (unused).
        _exc (Exception): The raised exception instance (unused).

    Returns:
        Response: A JSON-formatted error response indicating an invalid API key.
    """
    return ErrorJsonResponse(
        code=status.HTTP_403_FORBIDDEN,
        message="Invalid API key",
        status=ErrorStatus.PERMISSION_DENIED,
    )


async def not_found_exception_handler(
    _request: Request, _exc: Exception
) -> Response:
    """
    Handle the case when an invalid API key is provided.

    Returns a 403 Forbidden JSON response with an appropriate error message.

    Args:
        _request (Request): The incoming FastAPI request (unused).
        _exc (Exception): The raised exception instance (unused).

    Returns:
        Response: A JSON-formatted error response indicating an invalid API key.
    """
    return ErrorJsonResponse(
        code=status.HTTP_404_NOT_FOUND,
        message="Not found",
        status=ErrorStatus.NOT_FOUND,
    )


async def http_exception_handler(_request: Request, exc: Exception):
    """
    Handle unexpected HTTP exceptions.

    Logs the exception and returns a 500 Internal Server Error response.
    This serves as a fallback for unhandled exceptions during request processing.

    Args:
        _request (Request): The incoming FastAPI request (unused).
        exc (Exception): The caught exception instance.

    Returns:
        Response: A JSON-formatted error response representing an internal server error.
    """
    logger.error(
        "HTTPException: %s %s",
        status.HTTP_500_INTERNAL_SERVER_ERROR,
        exc,
    )

    return ErrorJsonResponse(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message="Internal server error",
        status=ErrorStatus.INTERNAL,
    )
