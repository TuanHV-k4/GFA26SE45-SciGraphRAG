"""Repository that reads local runtime health information."""

import platform
from datetime import UTC, datetime

from app.models.health import HealthRecord


class HealthRepository:
    """Read process-level health information."""

    def read(self) -> HealthRecord:
        """Build a health record from the running Python process."""
        return HealthRecord(
            status="ok",
            python_version=platform.python_version(),
            checked_at=datetime.now(UTC),
        )

