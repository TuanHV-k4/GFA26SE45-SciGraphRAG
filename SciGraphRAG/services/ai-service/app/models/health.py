"""Health-check domain model."""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal


@dataclass(frozen=True, slots=True)
class HealthRecord:
    """Internal representation of a successful process health check."""

    status: Literal["ok"]
    python_version: str
    checked_at: datetime

