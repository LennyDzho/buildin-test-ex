from dishka import make_async_container
from dishka.integrations.fastapi import DishkaRoute, FastapiProvider, setup_dishka
from fastapi import APIRouter, Depends, FastAPI

from .v1.incidents import IncidentsProvider, incidents_router
from ..guards import auth_guard

from ..providers.db_provider import DatabaseProvider

api_router = APIRouter(
    prefix="/api",
    route_class=DishkaRoute,
    dependencies=[Depends(auth_guard)]
)

api_router.include_router(incidents_router)

def setup_container(app: FastAPI) -> None:
    """
    Initializes and configures the Dishka dependency container for the FastAPI application.

    Creates an asynchronous container with FastapiProvider,
    DatabaseProvider providers, and so on.
    After that, it integrates it with the transferred FastAPI application.
    This container is used to inject dependencies into all endpoints
    registered via DishkaRoute.

     Args:
        app (FastAPI): The FastAPI instance that the container is configured for.

     Returns:
        None
     """
    container = make_async_container(
        FastapiProvider(),
        DatabaseProvider(),
        IncidentsProvider(),
    )

    setup_dishka(container, app)


__all__ = ["api_router", "setup_container"]
