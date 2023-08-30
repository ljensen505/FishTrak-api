from app.models.models import Lure
from .base import Controller


class LureController(Controller):
    def __init__(self) -> None:
        super().__init__()
        self.table = "Lure"

    def get_lures(self) -> list[Lure]:
        return [Lure(**l) for l in self._get_all()]
