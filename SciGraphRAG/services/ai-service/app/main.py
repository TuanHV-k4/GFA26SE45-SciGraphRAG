"""FastAPI application entry point."""

from fastapi import FastAPI

from app.controllers.health_controller import router as health_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    application = FastAPI(
        title=settings.name,
        version=settings.version,
        description="SciGraphRAG AI service",
    )
    application.include_router(health_router)
    return application


app = create_app()

