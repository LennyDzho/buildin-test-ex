from fastapi import Security

from fastapi.security.api_key import APIKey, APIKeyHeader

from src.core.infra.exceptions import NotApiKey, InvalidApiKey
from src.core.config.settings import settings


api_key_header = APIKeyHeader(
    name="x-api-key",
    auto_error=False,
    scheme_name="x-api-key",
    description="Авторизация по API key",
)


async def auth_guard(api_key: APIKey = Security(api_key_header)) -> APIKey:
    """
    Guard that enforces API-key authorization.

    Ensures that a request includes the header “x-api-key” and that its value
    matches the configured API key (settings.app.api_key). If the header is
    missing or the key is invalid, raises the respective exception.

    Args:
        api_key (APIKey): The API key value extracted from the “x-api-key” header via FastAPI’s
                         Security mechanism.

    Returns:
        APIKey: The validated API key.

    Raises:
        NotApiKey: If no API key header was provided.
        InvalidApiKey: If the provided API key does not match the expected value.
    """
    if not api_key:
        raise NotApiKey(detail="Api key not found")
    if api_key != settings.app.api_key:
        raise InvalidApiKey(detail="Invalid api key")
    return api_key
