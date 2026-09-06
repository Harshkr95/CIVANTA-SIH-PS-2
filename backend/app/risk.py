from fastapi import APIRouter
import csv
import os

router = APIRouter()

CSV_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../ml-risk-engine/outputs/road_risk_scores.csv"
)


@router.get("/risk")
def get_risk_scores():
    with open(CSV_PATH, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
