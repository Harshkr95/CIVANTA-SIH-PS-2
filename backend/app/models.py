from sqlalchemy import Column, DateTime, Float, Integer, String
from datetime import datetime

from .database import Base


class RiskScore(Base):
    __tablename__ = "risk_scores"

    id = Column(Integer, primary_key=True, index=True)
    road_id = Column(String, unique=True, index=True, nullable=False)
    risk_score = Column(Float, nullable=False)
    predicted_disruption = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    # Used when the account is linked to Google.
    google_id = Column(String, unique=True, index=True, nullable=True)

    # Used only if email/password authentication is retained.
    password_hash = Column(String, nullable=True)

    role = Column(String, nullable=False, default="user")
    language = Column(String, nullable=False, default="en")
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
from sqlalchemy import Column, Float, Integer, String
from .database import Base



