from logging import Logger
from typing import Optional, Any


class AppException(Exception):
    """
    Base application exception with optional detail, code, and extra context.

    Provides a structured way to raise errors with descriptive messages,
    error codes, and arbitrary additional information. Includes a method
    to log the exception via a provided logger.
    """
    detail: Optional[str]
    code: Optional[str]
    extra: dict

    def __init__(
        self, detail: Optional[str] = None, code: Optional[str] = None, **extra: Any
    ):
        """
        Initialize the application exception.

        Args:
            detail (Optional[str]): Human-readable description of the error.
            code (Optional[str]): Optional machine-readable error code.
            **extra (Any): Additional keyword arguments providing context.
        """
        self.detail = detail
        self.code = code
        self.extra = extra
        super().__init__(detail)

    def __str__(self) -> str:
        """
        Return a string representation of the exception, including
        the class name, detail, code, and extra information.

        Returns:
            str: Formatted exception string.
        """
        code_part = f" [{self.code}]" if self.code else ""
        extra_part = f" | {self.extra}" if self.extra else ""
        return f"{self.__class__.__name__}: {self.detail or ''}{code_part}{extra_part}"

    def log(self, logger: Logger) -> None:
        """
        Log the exception using the provided logger at error level.

        Args:
            logger (Logger): A logging.Logger instance.
        """
        logger.error(str(self))


class NotApiKey(AppException):
    """Exception raised when API key authorization is missing."""


class InvalidApiKey(AppException):
    """Exception raised when an invalid API key is provided."""


class NotFound(AppException):
    """Exception raised when a requested record is not found."""


class Conflict(AppException):
    """Exception raised when there is a data conflict (e.g., duplicate entry)."""
