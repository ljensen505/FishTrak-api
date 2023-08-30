from fastapi.testclient import TestClient
from app.main import app
from httpx import Response

client = TestClient(app)
route = "species/"


def test_species() -> None:
    res: Response = client.get(f"/{route}")
    assert res.status_code == 200
    data: list[dict] = res.json()
    assert len(data) >= 2
    for species in data:
        attrs = ["species_id", "name", "avg_weight", "is_freshwater", "description"]
        for attr in attrs:
            assert species.get(attr) is not None
