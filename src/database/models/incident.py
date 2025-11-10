from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    Enum as SqlEnum,
)
from sqlalchemy.dialects.postgresql import TIMESTAMP

from src.database.models import Base
from src.database.models.enums import IncidentStatus, IncidentSource


class Incident(Base):
    """
    Database model representing an incident.

    Attributes:
        id (int): Primary key.
        description (str): Text description of the incident.
        status (IncidentStatus): Current status of the incident.
        source (IncidentSource): Origin of the incident.
        created_at (datetime): Timestamp of creation.
    """
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text, nullable=False)
    status = Column(SqlEnum(IncidentStatus), default=IncidentStatus.NEW, nullable=False)
    source = Column(SqlEnum(IncidentSource), nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        default=datetime.now(timezone.utc),
        nullable=False,
    )