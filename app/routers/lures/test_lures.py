from fastapi.testclient import TestClient
from app.main import app
from httpx import Response

client = TestClient(app)
route = "lures/"


def test_lures() -> None:
    res: Response = client.get(f"/{route}")
    assert res.status_code == 200
    data: list[dict] = res.json()
    assert len(data) >= 2
    for lure in data:
        attrs = ["lure_id", "weight", "name", "color", "type"]
        for attr in attrs:
            assert lure.get(attr) is not None
