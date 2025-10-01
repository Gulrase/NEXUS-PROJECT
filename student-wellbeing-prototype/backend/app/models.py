from sqlalchemy import Column, String, Integer, Float, DateTime, JSON, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from .db import Base
import sqlalchemy as sa

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sa.text("gen_random_uuid()"))
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    role = Column(String, default="student")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    consent_given = Column(sa.Boolean, default=False)

# (Other SQLAlchemy model definitions can be added if needed)
