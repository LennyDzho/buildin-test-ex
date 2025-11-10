from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict

from src.database.models.enums import IncidentStatus, IncidentSource


class IncidentData(BaseModel):
    """Data model for an incident."""
    id: int
    description: str
    status: IncidentStatus
    source: IncidentSource
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CreateIncidentRequest(BaseModel):
    """Request schema for creating a new incident."""
    description: str
    status: IncidentStatus = Field(default=IncidentStatus.NEW)
    source: IncidentSource


class UpdateIncidentStatusRequest(BaseModel):
    """Request schema for updating the status of an incident."""
    incident_id: int
    status: IncidentStatus


class ListIncidentsResponse(BaseModel):
    """Response schema for returning a list of incidents."""
    incidents: List[IncidentData]


class IncidentResponse(BaseModel):
    """Response schema for a single incident."""
    incident: IncidentData
