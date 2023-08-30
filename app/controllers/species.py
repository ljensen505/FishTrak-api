from app.models.models import Species
from .base import Controller


class SpeciesController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self.table = "Species"

    def get_all_species(self) -> list[Species]:
        return [Species(**s) for s in self._get_all()]
