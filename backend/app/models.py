from sqlalchemy import Column, Float, Integer, String
from .database import Base


class RiskScore(Base):
    __tablename__ = "risk_scores"

    id = Column(Integer, primary_key=True, index=True)
    road_id = Column(String, unique=True, index=True, nullable=False)
    risk_score = Column(Float, nullable=False)
    predicted_disruption = Column(Integer, nullable=False)

