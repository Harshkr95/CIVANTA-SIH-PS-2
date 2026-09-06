from fastapi import APIRouter

router = APIRouter()


roads = [
    {
        "id": 1,
        "name": "NH-10",
        "district": "Gangtok",
        "status": "OPEN",
        "risk_level": "LOW",
    },
    {
        "id": 2,
        "name": "NH-6",
        "district": "Aizawl",
        "status": "BLOCKED",
        "risk_level": "HIGH",
    },
    {
        "id": 3,
        "name": "NH-37",
        "district": "Guwahati",
        "status": "OPEN",
        "risk_level": "MEDIUM",
    },
    {
        "id": 4,
        "name": "NH-29",
        "district": "Kohima",
        "status": "PARTIALLY_BLOCKED",
        "risk_level": "HIGH",
    },
]


@router.get("/roads")
def get_roads():
    return roads

@router.get("/roads/{road_id}")
def get_road(road_id: int):
    for road in roads:
        if road["id"] == road_id:
            return road

    return {"error": "Road not found"}
