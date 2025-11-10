from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound

from src.api.v1.incidents.scheams import IncidentData
from src.core.infra.exceptions import NotFound
from src.database.models.enums import IncidentStatus
from src.database.repositories.incident_repo import IncidentRepo


class IncidentService:
    """
    Service layer for handling incident operations.

    Wraps IncidentRepo to provide business logic for creation,
    listing, and status updates.
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.repo = IncidentRepo(session)

    async def create_incident(
        self, description: str, status: IncidentStatus, source: str
    ) -> IncidentData:
        """Create a new incident."""
        incident = await self.repo.create_incident(
            description=description,
            status=status,
            source=source,
        )
        return IncidentData.model_validate(incident)

    async def list_incidents(
        self, status: Optional[IncidentStatus] = None
    ) -> List[IncidentData]:
        """List incidents, optionally filtered by status."""
        incidents = await self.repo.list_incidents(status=status)
        return [IncidentData.model_validate(incident) for incident in incidents]

    async def update_status(
        self, incident_id: int, new_status: IncidentStatus
    ) -> IncidentData:
        """Update the status of an incident by ID. Raises NotFound if not exists."""
        try:
            incident = await self.repo.update_status(
                incident_id=incident_id, new_status=new_status
            )
        except NoResultFound:
            raise NotFound(f"Incident with id {incident_id} not found.")

        return IncidentData.model_validate(incident)
