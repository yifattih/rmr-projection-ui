import pytest
from main import service

collect_ignore = ["otel/"]

collect_ignore_glob = ["otel/*"]


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
