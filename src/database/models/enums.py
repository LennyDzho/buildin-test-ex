from enum import Enum


class IncidentStatus(str, Enum):
    """Possible statuses for an incident."""
    NEW = "new"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IncidentSource(str, Enum):
    """Possible sources for an incident."""
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"
    