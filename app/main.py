from fastapi import FastAPI

from app.routers.fishermen.fishermen import router as fishermen_router
from app.routers.species.species import router as species_router
from app.routers.lures.lures import router as lure_router

app = FastAPI()

app.include_router(fishermen_router, prefix="/fishermen")
app.include_router(species_router, prefix="/species")
app.include_router(lure_router, prefix="/lures")


@app.get("/")
async def root():
    return {"message": "FishTrak API"}
