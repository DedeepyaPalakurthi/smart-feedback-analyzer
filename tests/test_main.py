from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_post():
    response = client.post("/predict", json={"text": "I love this product!"})
    assert response.status_code == 200
    assert "label" in response.json()
