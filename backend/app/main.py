from app.api import routes_cve, routes_health
from app.core.config import settings
from app.core.logger import get_logger
from fastapi import FastAPI

logger = get_logger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-powered Vulnerability Intelligence Platform",
)

# include routes
app.include_router(routes_health.router, prefix="", tags=["Health"])
app.include_router(routes_cve.router, prefix="/api", tags=["CVE"])


@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.APP_NAME} (env={settings.ENVIRONMENT})")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"Shutting down {settings.APP_NAME}")
