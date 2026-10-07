from datetime import UTC, datetime

from app.models.health import HealthRecord
from app.services.health_service import HealthService


class StubHealthRepository:
    def __init__(self, record: HealthRecord) -> None:
        self.record = record
        self.calls = 0

    def read(self) -> HealthRecord:
        self.calls += 1
        return self.record


def test_health_service_delegates_to_repository() -> None:
    expected = HealthRecord(
        status="ok",
        python_version="3.12.10",
        checked_at=datetime(2026, 10, 4, tzinfo=UTC),
    )
    repository = StubHealthRepository(expected)
    service = HealthService(repository=repository)

    assert service.get_health() == expected
    assert repository.calls == 1
