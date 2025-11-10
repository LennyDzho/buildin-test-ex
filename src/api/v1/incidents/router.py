from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends, HTTPException, status

from src.core.infra.exceptions import NotFound

from .scheams import (
    IncidentResponse,
    CreateIncidentRequest,
    ListIncidentsResponse,
    UpdateIncidentStatusRequest,
)
from .services import IncidentService


router = APIRouter(
    prefix="/incidents",
    tags=["incidents"],
    route_class=DishkaRoute,
)


# ----- CREATE -----
@router.post(
    "",
    response_model=IncidentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_incident(
    data: CreateIncidentRequest,
    service: FromDishka[IncidentService],
) -> IncidentResponse:
    incident = await service.create_incident(
        description=data.description,
        status=data.status,
        source=data.source,
    )
    return IncidentResponse(incident=incident)


# ----- LIST -----
@router.get(
    "",
    response_model=ListIncidentsResponse,
)
async def list_incidents(
    service: FromDishka[IncidentService],
    status: str | None = None,
) -> ListIncidentsResponse:
    incidents = await service.list_incidents(
        status=status if status is None else status
    )
    return ListIncidentsResponse(incidents=incidents)


# ----- UPDATE STATUS -----
@router.patch(
    "/{incident_id}/status",
    response_model=IncidentResponse,
)
@router.patch(
    "/status",
    response_model=IncidentResponse,
)
async def update_incident_status(
    body: UpdateIncidentStatusRequest,
    service: FromDishka[IncidentService],
) -> IncidentResponse:
    incident = await service.update_status(
        incident_id=body.incident_id,
        new_status=body.status,
    )
    return IncidentResponse(incident=incident)

