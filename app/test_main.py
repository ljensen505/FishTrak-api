from fastapi.testclient import TestClient
from app.main import app
from httpx import Response

client = TestClient(app)


def test_root():
    res: Response = client.get("/")
    assert res.status_code == 200
    assert res.json().get("message") == "FishTrak API"
