"""Health-check response schemas."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    """Public response returned by the health endpoint."""

    model_config = ConfigDict(from_attributes=True)

    status: Literal["ok"]
    python_version: str
    checked_at: datetime

