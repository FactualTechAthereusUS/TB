"""
Database connection and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from config import settings
import os

# Create database directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create base for all models
Base = declarative_base()

# Create database engine
DATABASE_URL = settings.DATABASE_URL
engine = create_engine(
    DATABASE_URL,
    echo=False
)
print(f"🔌 Connecting to database: {DATABASE_URL.split('@')[-1]}")  # Log host/db only for security

# Enable pgvector extension
from sqlalchemy import text
with engine.connect() as conn:
    try:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    except Exception as e:
        print(f"Warning: Could not enable pgvector extension: {e}")

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initialize database - create all tables"""
    # Import models to register them with Base
    from models.chat import Chat, Message
    from models.user import User
    from models.document import DocumentChunk
    from models.ingestion import IngestionStatus
    
    # Create all tables
    Base.metadata.create_all(bind=engine)

