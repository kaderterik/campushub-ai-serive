import pytest
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_classify_success():
    response = client.post(
        "/ai/classify",
        json={"text": "Python atölyesi"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "category": "TECHNOLOGY",
        "confidence": 0.91,
    }


@pytest.mark.parametrize(
    "payload",
    [
        {"text": ""},
        {"text": "   "},
        {},
        {"text": 123},
        {"text": None},
    ],
)
def test_classify_invalid_input(payload):
    response = client.post("/ai/classify", json=payload)

    assert response.status_code == 400
    body = response.json()
    assert body["error"] == "VALIDATION_ERROR"
    assert isinstance(body["message"], str)
    assert body["message"]


def test_classify_invalid_json():
    response = client.post(
        "/ai/classify",
        content='{"text":',
        headers={"Content-Type": "application/json"},
    )

    assert response.status_code == 400
    assert response.json()["error"] == "VALIDATION_ERROR"