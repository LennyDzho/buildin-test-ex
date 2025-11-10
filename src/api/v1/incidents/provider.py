from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from .services import IncidentService


class IncidentsProvider(Provider):
    """
    Dishka provider for IncidentService.
    Each request gets its own service instance.
    """
    scope = Scope.REQUEST

    @provide
    async def service(self, session: AsyncSession) -> IncidentService:
        return IncidentService(session)
