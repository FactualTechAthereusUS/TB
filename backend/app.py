"""
TradeBerg Backend API
Main FastAPI application for React frontend
"""
import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from config import settings
from routes import api_router
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    # Startup
    print("🚀 Starting TradeBerg Backend API...")
    print(f"📡 Environment: {settings.ENVIRONMENT}")
    print(f"🌐 CORS Origins: {settings.get_cors_origins()}")
    
    # Initialize database
    init_db()
    print("✅ Database initialized")

    # Start Ingestion Worker in background
    import asyncio
    from core.ingestion.pipeline import pipeline
    loop = asyncio.get_running_loop()
    loop.create_task(pipeline.start(poll_interval=5))
    print("👷 Ingestion Worker background task started")
    
    yield
    # Shutdown
    print("👋 Shutting down TradeBerg Backend API...")

# Create FastAPI app
app = FastAPI(
    title="TradeBerg API",
    description="Backend API for TradeBerg Trading Platform",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    """Root endpoint"""
    return JSONResponse({
        "message": "TradeBerg API",
        "version": "1.0.0",
        "status": "running"
    })

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return JSONResponse({
        "status": "healthy",
        "service": "TradeBerg API"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

