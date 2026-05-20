from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_rate():
    payload = {
        'comment':"good"
    }
    for _ in range(6):
        response = client.post(
            "/predict",
            json = payload
        )
    assert response.status_code == 429