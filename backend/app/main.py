from fastapi import FastAPI
from app.roads import router as roads_router
from app.risk import router as risk_router


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "CIVANTA-NER Backend is running!"
    }


app.include_router(roads_router)
app.include_router(risk_router)

