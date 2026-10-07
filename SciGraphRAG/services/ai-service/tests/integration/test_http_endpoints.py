import asyncio

import httpx

from app.main import app


def test_health_endpoint() -> None:
    async def request() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            return await client.get("/health")

    response = asyncio.run(request())
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["python_version"].startswith("3.12.")
    assert payload["checked_at"]


def test_docs_and_openapi_are_available() -> None:
    async def request() -> tuple[httpx.Response, httpx.Response]:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            return await client.get("/docs"), await client.get("/openapi.json")

    docs_response, schema_response = asyncio.run(request())
    assert docs_response.status_code == 200
    assert "Swagger UI" in docs_response.text
    assert schema_response.status_code == 200
    assert "/health" in schema_response.json()["paths"]
