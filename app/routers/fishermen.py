from fastapi import APIRouter, status
from app.models.models import Fisherman
from app.db import db_conn

router = APIRouter()
TABLE = "Fisherman"


@router.get("/", response_model=list[Fisherman])
async def all_fishermen() -> list[Fisherman]:
    # this is just an example for interacting with the db
    # we should move all "query" logic to its own class within its own file
    # we could then call something like: Fishermen.get_all() or Fishermen.get_one(fisherman_id)
    cursor = db_conn.cursor()
    query = f"SELECT * FROM {TABLE}"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db_conn.close()
    return [Fisherman(fisherman_id=f[0], name=f[1]) for f in result] if result else []
