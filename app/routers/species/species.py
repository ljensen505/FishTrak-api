from fastapi import APIRouter, status
from app.models.models import Species
from app.controllers.species import SpeciesController

router = APIRouter()
controller = SpeciesController()


@router.get("/", response_model=list[Species])
async def all_species() -> list[Species]:
    return controller.get_all_species()
