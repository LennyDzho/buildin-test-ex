from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Base


class BaseRepo:
    """
    Base repository providing common database operations for SQLAlchemy ORM models.

    This class wraps an asynchronous SQLAlchemy session and provides
    basic CRUD operations that can be used or extended by specific repositories.
    """

    def __init__(self, session: AsyncSession) -> None:
        """
        Initialize the repository with an asynchronous database session.

        Args:
            session (AsyncSession): An async SQLAlchemy session instance.
        """
        self.session = session

    def add(self, obj: Base) -> None:
        """
        Add a new object to the session.

        Args:
            obj (Base): An instance of a SQLAlchemy ORM model to add.
        """
        self.session.add(obj)

    async def delete(self, obj: Base) -> None:
        """
        Delete an object from the database session.

        Args:
            obj (Base): An instance of a SQLAlchemy ORM model to delete.
        """
        await self.session.delete(obj)

    async def commit(self) -> None:
        """
        Commit the current transaction to the database.
        """
        await self.session.commit()

    async def rollback(self) -> None:
        """
        Roll back the current transaction in case of an error.
        """
        await self.session.rollback()
