from fastapi import APIRouter, status
from app.models.models import Lure
from app.controllers.lures import LureController

router = APIRouter()
controller = LureController()


@router.get("/", response_model=list[Lure])
async def all_lures() -> list[Lure]:
    return controller.get_lures()
