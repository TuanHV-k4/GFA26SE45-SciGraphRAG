"""Health-check HTTP controller."""

from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.schemas.health import HealthResponse
from app.services.health_service import HealthService, get_health_service

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Check service health",
)
def get_health(
    service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    """Return the current process health status."""
    return HealthResponse.model_validate(service.get_health())

