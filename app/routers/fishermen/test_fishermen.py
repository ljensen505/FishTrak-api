from fastapi.testclient import TestClient
from app.main import app
from httpx import Response

client = TestClient(app)
route = "fishermen/"


def test_root() -> None:
    res: Response = client.get(f"/{route}")
    assert res.status_code == 200
    data: list[dict] = res.json()
    assert len(data) >= 3
    for fisherman in data:
        attrs = ["fisherman_id", "name"]
        for attr in attrs:
            assert fisherman.get(attr) is not None
