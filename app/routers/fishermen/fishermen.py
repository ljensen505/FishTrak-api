from fastapi import APIRouter, status
from app.models.models import Fisherman
from app.controllers.fishermen import FishermanController

router = APIRouter()
controller = FishermanController()


@router.get("/", response_model=list[Fisherman])
async def all_fishermen() -> list[Fisherman]:
    return controller.get_fishermen()
