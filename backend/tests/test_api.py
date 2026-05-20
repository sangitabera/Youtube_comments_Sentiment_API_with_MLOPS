from fastapi.testclient import TestClient
from backend.app import app


client = TestClient(app)

# testing home route
def test_home():
    response = client.get("/")
    assert response.status_code == 200

# testing predict route
def test_predict():
    payload = {
        'comment':"This video is amazing"
    }
    response = client.post(
        "/predict",
        json = payload
    )
    assert response.status_code == 200
    data = response.json()
    assert "Sentiment" in data

# testing explain route
def explain_predict():
    payload = {
        'comment':'worst video video ever'
    }
    response = client.post(
        "/explain",
        json = payload
    )
    assert response.status_code == 200
    data = response.json()

    assert "prediction" in data
    assert "explanation" in data