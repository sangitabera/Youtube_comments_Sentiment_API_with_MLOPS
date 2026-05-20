from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)

def test_empty_comment():
    payload = {
        'comment':''
    }
    response = client.post(
        "/predict",
        json = payload
    )

    assert response.status_code == 422