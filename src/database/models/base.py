from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Abstract base class for all SQLAlchemy ORM models.

    Inherits from SQLAlchemy's DeclarativeBase and sets the class
    as abstract so that no table is created for this base class itself.
    All application models should inherit from this class to share
    common metadata and configurations.
    """
    __abstract__ = True
