from pydantic import BaseModel
from typing import Optional


class Fisherman(BaseModel):
    # TODO: it would be nice to have this use a uuid rather than an int for id
    # this goes for all tables in the db
    # This would require updating the DDL file, which might be super annoying
    # str(uuid.uuid4())
    fisherman_id: int
    name: str


class Species(BaseModel):
    species_id: int
    name: str
    avg_weight: float
    is_freshwater: bool
    description: Optional[str] = None


class WaterBody(BaseModel):
    body_id: int
    name: str
    is_freshwater: bool
    is_stocked: bool
    latitude: float
    longitude: float


class Lure(BaseModel):
    lure_id: int
    weight: float
    name: str
    color: str
    type: str


class CaughtFish(BaseModel):
    pass
