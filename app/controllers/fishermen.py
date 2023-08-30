from app.models.models import Fisherman
from .base import Controller


class FishermanController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self.table = "Fisherman"

    def get_fishermen(self) -> list[Fisherman]:
        return [Fisherman(**f) for f in self.get_all()]
