from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import RiskScore

router = APIRouter()


@router.get("/risk")
def get_risk_scores(db: Session = Depends(get_db)):
    risks = db.query(RiskScore).all()

    return [
        {
            "road_id": risk.road_id,
            "risk_score": risk.risk_score,
            "predicted_disruption": risk.predicted_disruption,
        }
        for risk in risks
    ]


@router.get("/risk/{road_id:path}")
def get_risk_score(
    road_id: str,
    db: Session = Depends(get_db),
):
    risk = (
        db.query(RiskScore)
        .filter(RiskScore.road_id == road_id)
        .first()
    )

    if not risk:
        raise HTTPException(
            status_code=404,
            detail="Road risk score not found",
        )

    return {
        "road_id": risk.road_id,
        "risk_score": risk.risk_score,
        "predicted_disruption": risk.predicted_disruption,
    }
