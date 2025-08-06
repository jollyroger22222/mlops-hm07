from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_predict_status_code():
    response = client.post("/predict", json={"passwords": ["123456", "password123"]})
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], list)
