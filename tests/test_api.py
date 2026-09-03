from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_analyze_resume():
    response = client.post(
        "/analyze",
        json={
            "text": "I work with Python, FastAPI and AWS."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "Python" in data["skills"]
    assert "FastAPI" in data["skills"]
    assert "AWS" in data["skills"]