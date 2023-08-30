from pydantic import BaseModel


class Fisherman(BaseModel):
    fisherman_id: int
    name: str
