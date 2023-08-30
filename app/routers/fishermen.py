from fastapi import APIRouter, status
from app.models.models import Fisherman
from app.db import db_conn

router = APIRouter()
TABLE = "Fisherman"


@router.get("/", response_model=list[Fisherman])
async def all_fishermen() -> list[Fisherman]:
    cursor = db_conn.cursor()
    query = f"SELECT * FROM {TABLE}"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    db_conn.close()
    return [Fisherman(fisherman_id=f[0], name=f[1]) for f in result] if result else []
