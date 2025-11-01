from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:password@localhost/mydb"

# Create the engine (connects SQLAlchemy to PostgreSQL)
engine = create_engine(DATABASE_URL)

# Create session factory (handles DB operations)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for ORM models
Base = declarative_base()
