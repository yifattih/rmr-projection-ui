from unittest.mock import MagicMock, patch

import pytest
from main import service
from requests.exceptions import ConnectionError


@pytest.fixture
def client():
    service.config["TESTING"] = True
    with service.test_client() as client:
        yield client


@pytest.fixture
def valid_data():
    return {
        "sex": "male",
        "units": "imperial",
        "age": "34",
        "weight": "71",
        "height": "198",
        "weight_loss_rate": 2,
        "duration": 30,
    }


@pytest.fixture
def invalid_data():
    return {
        "age": "abc",  # Invalid age
        "weight": "70",
        "height": "175",
        "sex": "male",
    }


def test_root_endpoint(client):
    """
    Test that the root endpoint returns a 200 status code
    """
    response = client.get("/")
    assert response.status_code == 200


def test_submit_valid_data(client, valid_data):
    """
    Test submitting valid data returns a 200 status code and correct RMR value
    """
    with patch("requests.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"rmr": 1700}
        mock_post.return_value = mock_response

        response = client.post("/submit/", data=valid_data)
        assert response.status_code == 200
        assert response.json == {"rmr": 1700}


def test_submit_invalid_data(client, invalid_data):
    """
    Test submitting invalid data returns a 400 status code and error message
    """
    response = client.post("/submit/", data=invalid_data)
    assert response.status_code == 400
    assert "Invalid input data" in response.json["message"]


def test_submit_api_failure(client, valid_data):
    """
    Test that API failure during submission returns a 500 status code and
    error message
    """
    with patch("requests.post", side_effect=ConnectionError):
        response = client.post("/submit/", data=valid_data)
        assert response.status_code == 503
        assert "Failed to contact API" in response.json["error"]


def test_health_check(client):
    """
    Test that the health check endpoint returns a 200 status code and healthy
    status
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert "timestamp" in response.json
    assert "uptime_utc" in response.json
