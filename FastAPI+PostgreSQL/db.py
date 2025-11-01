

from sqlalchemy import create_engine        # Connects Python to our database
from sqlalchemy.ext.declarative import declarative_base     # To define tables using Python classes
from sqlalchemy.orm import sessionmaker     # To interact with the database

# PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:Monday%40123@localhost/ROOKIES"

# Create the engine (connects SQLAlchemy to PostgreSQL)
engine = create_engine(DATABASE_URL)

# Create session factory (handles DB operations)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for ORM models
Base = declarative_base()
