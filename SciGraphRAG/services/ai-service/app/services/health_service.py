"""Health-check business service."""

from functools import lru_cache
from typing import Protocol

from app.models.health import HealthRecord
from app.repositories.health_repository import HealthRepository


class HealthRepositoryProtocol(Protocol):
    """Repository behavior required by the health service."""

    def read(self) -> HealthRecord:
        """Return current process health information."""
        ...


class HealthService:
    """Coordinate the health-check use case."""

    def __init__(self, repository: HealthRepositoryProtocol) -> None:
        self._repository = repository

    def get_health(self) -> HealthRecord:
        """Return health data supplied by the repository layer."""
        return self._repository.read()


@lru_cache
def get_health_service() -> HealthService:
    """Provide a reusable health service for FastAPI dependency injection."""
    return HealthService(repository=HealthRepository())
