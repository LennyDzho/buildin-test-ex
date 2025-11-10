__all__ = ["settings", "setup_logging", "lifespan",]

from src.core.config.settings import settings
from .lifespan import lifespan
from src.core.config.log_setup import setup_logging
