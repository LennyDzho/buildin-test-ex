from typing import AsyncGenerator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from ..database.helper import db_helper


class DatabaseProvider(Provider):
    """
    Dishka provider for asynchronous database sessions.

    This provider manages the lifecycle of SQLAlchemy async sessions
    with request scope, ensuring that each request receives its own session.
    """
    scope = Scope.REQUEST

    @provide
    async def provide_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Provide an asynchronous SQLAlchemy session for a request.

        Yields:
            AsyncSession: A new asynchronous session instance from the
            global DatabaseHelper session factory.
        """
        async with db_helper.session_factory() as session:
            yield session
