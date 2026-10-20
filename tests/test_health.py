from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_returns_200():
    response = client.get("/health")

    assert response.status_code == 200


def test_health_response_schema():
    response = client.get("/health")
    body = response.json()

    assert set(body.keys()) == {"service", "status", "version"}
    assert all(isinstance(value, str) for value in body.values())


def test_health_response_values():
    response = client.get("/health")

    assert response.json() == {
        "service": "ai-service",
        "status": "UP",
        "version": "1.0.0",
    }
