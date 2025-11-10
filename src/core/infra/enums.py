from enum import Enum


class ErrorStatus(str, Enum):
    """
    Enumeration of standardized application error statuses.

    Defines a consistent set of error identifiers used in API responses
    to indicate the type of failure that occurred.
    """
    NOT_FOUND = "NOT_FOUND"
    UNAUTHENTICATED = "UNAUTHENTICATED"
    PERMISSION_DENIED = "PERMISSION_DENIED"
    INTERNAL = "INTERNAL"
