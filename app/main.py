from fastapi import FastAPI

from app.routers.fishermen import router as fishermen_router
from dotenv import load_dotenv

app = FastAPI()

app.include_router(fishermen_router, prefix="/fishermen")


@app.get("/")
async def root():
    return {"message": "FishTrak API"}
