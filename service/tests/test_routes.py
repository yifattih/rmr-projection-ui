import pytest
from ..main import app
import subprocess
import time

# Constants
API_TEST_URL = "http://localhost:4000"  # Test API server URL


@pytest.fixture(scope="module", autouse=True)
def api_server():
    """
    Start a test API server as a subprocess.

    Yields
    ------
    None

    Notes
    -----
    This starts a simple mock API server for testing at port 5001.
    """
    process = subprocess.Popen(["python", "test_api_server.py"])
    time.sleep(1)  # Wait for server to start
    yield
    process.terminate()


@pytest.fixture
def client():
    """
    Flask test client for making requests.

    Returns
    -------
    FlaskClient
        A test client for the Flask application.
    """
    app.config["TESTING"] = True
    app.config["API_URL"] = API_TEST_URL
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """
    Test the homepage route.

    Parameters
    ----------
    client : FlaskClient
        Flask test client.

    Asserts
    -------
    Status code : int
        Should be 200 for GET requests to `/`.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"<!DOCTYPE html>" in response.data  # Verify content.


def test_submit_route_missing_data(client):
    """
    Test the `submit` route with missing form data.

    Parameters
    ----------
    client : FlaskClient
        Flask test client.

    Asserts
    -------
    Status code : int
        Should be 400 for missing data.
    Response : dict
        Should contain error messages.
    """
    form_data = {
        "sex": "",
        "units": "si",
        "age": "30",
        "weight": "70",
        "height": "175",
        "weight_loss_rate": "1",
        "duration": "30",
    }
    response = client.post("/submit", data=form_data)
    assert response.status_code == 400
    assert "Missing value for sex" in response.json["error"]


def test_submit_route_api_failure(client):
    """
    Test the `submit` route with an unreachable API.

    Parameters
    ----------
    client : FlaskClient
        Flask test client.

    Asserts
    -------
    Status code : int
        Should be 500 for API connection failure.
    Response : dict
        Should contain error message.
    """
    app.config["API_URL"] = "http://127.0.0.1:9999"  # Non-existing server
    form_data = {
        "sex": "male",
        "units": "metric",
        "age": "30",
        "weight": "70",
        "height": "175",
        "weight_loss_rate": "1",
        "duration": "30",
    }
    response = client.post("/submit", data=form_data)
    assert response.status_code == 500
    assert "Failed to contact API" in response.json["error"]
