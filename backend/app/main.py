from fastapi import FastAPI

from app.database import engine, Base

from app.routers.auth import router as auth_router

from app.routers.homes import router as homes_router

# Import all models before creating tables
from app.models import (
    User,
    Home,
    HomeMember,
    ApplianceCategory,
    Appliance,
    ApplianceDocument
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HomeCare API",
    description="Smart Home Management System",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(homes_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to HomeCare API",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "application": "HomeCare",
        "status": "Healthy"
    }
