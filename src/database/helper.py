import logging
from typing import AsyncGenerator

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from src.core.config.settings import settings


logger = logging.getLogger(__name__)


class DatabaseHelper:
    """
    Helper class for managing synchronous and asynchronous SQLAlchemy database connections.

    Provides:
        - Synchronous and asynchronous engines
        - Async session factory
        - Methods to get sessions and dispose of the async engine
    """

    def __init__(
        self,
        url: str,
        echo: bool = False,
        echo_pool: bool = False,
        pool_size: int = 10,
        max_overflow: int = 10,
    ) -> None:
        """
        Initialize the DatabaseHelper with connection parameters.

        Args:
            url (str): Database connection URL.
            echo (bool): If True, SQLAlchemy will log all statements. Defaults to False.
            echo_pool (bool): If True, SQLAlchemy will log connection pool events. Defaults to False.
            pool_size (int): The size of the connection pool. Defaults to 10.
            max_overflow (int): Maximum number of connections above the pool size. Defaults to 10.
        """
        self.engine: Engine = create_engine(
            url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.async_engine: AsyncEngine = create_async_engine(
            url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.session_factory = async_sessionmaker(
            bind=self.async_engine, expire_on_commit=False, autoflush=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Create an asynchronous database session for use in a context manager.

        Yields:
            AsyncSession: An active asynchronous SQLAlchemy session.
        """
        logger.debug("Creating new database session...")
        async with self.session_factory() as session:
            yield session

    async def dispose(self) -> None:
        """
        Dispose of the asynchronous engine and release all resources.

        This should be called during application shutdown to close
        all active connections cleanly.
        """
        logger.info("Disposing database...")
        await self.async_engine.dispose()


db_helper: DatabaseHelper = DatabaseHelper(
    settings.db.connection_url(),
    echo=False,
    echo_pool=False,
    pool_size=10,
    max_overflow=50,
)
"""Global instance of DatabaseHelper configured with application settings."""
