import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from ..database.helper import db_helper


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """
    Async context manager for FastAPI application lifespan.

    Handles startup and shutdown routines for the application, including:
        - Logging startup and shutdown events.
        - Disposing of the database connection helper.
        - Closing the Dishka dependency injection container.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: Control is yielded to allow the application to run during its lifespan.
    """

    # Startup
    logger.info("Starting application....")
    yield
    # Shutdown
    await db_helper.dispose()
    await app.state.dishka_container.close()

    logger.info("Application shutdown complete.")
