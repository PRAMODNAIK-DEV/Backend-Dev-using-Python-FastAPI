from sqlalchemy import Column, Integer, String
from db import Base

class User(Base):
    __tablename__ = "users"   # Table name in DB

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(200))
    test_id = Column(Integer)