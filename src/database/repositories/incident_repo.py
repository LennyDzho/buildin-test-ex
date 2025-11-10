from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.database.models import Incident
from src.database.models.enums import IncidentStatus
from src.database.repositories import BaseRepo


class IncidentRepo(BaseRepo):
    """
    Repository for operations on Incident table.
    """

    async def create_incident(
        self,
        *,
        description: str,
        status: IncidentStatus,
        source: str,
    ) -> Incident:
        """
        Create a new incident and commit it to the database.

        Args:
            description (str): Text description of the incident.
            status (IncidentStatus): Initial status of the incident.
            source (str): Origin of the incident (operator/monitoring/partner).

        Returns:
            Incident: The created Incident instance.
        """
        incident = Incident(
            description=description,
            status=status,
            source=source,
            created_at=datetime.now(timezone.utc),
        )
        self.add(incident)
        await self.commit()
        return incident

    async def list_incidents(
        self, *, status: Optional[IncidentStatus] = None
    ) -> List[Incident]:
        """
        Get a list of incidents, optionally filtered by status.

        Args:
            status (Optional[IncidentStatus]): Filter incidents by status.

        Returns:
            List[Incident]: List of Incident objects.
        """
        stmt = select(Incident)
        if status:
            stmt = stmt.where(Incident.status == status)

        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update_status(
        self, *, incident_id: int, new_status: IncidentStatus
    ) -> Incident:
        """
        Update the status of an incident by ID.

        Args:
            incident_id (int): ID of the incident to update.
            new_status (IncidentStatus): New status to set.

        Raises:
            NoResultFound: If no incident with the given ID exists.

        Returns:
            Incident: The updated Incident instance.
        """
        stmt = select(Incident).where(Incident.id == incident_id)
        result = await self.session.execute(stmt)
        incident = result.scalar_one_or_none()

        if not incident:
            raise NoResultFound(f"Incident with id {incident_id} not found.")

        incident.status = new_status
        await self.commit()
        return incident
