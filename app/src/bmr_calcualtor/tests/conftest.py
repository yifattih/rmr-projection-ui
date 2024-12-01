import pytest
from time_projection import TimeProjection  # noqa
from equations import Equations  # noqa
from model import RMRModel  # noqa


@pytest.fixture
def time_projection() -> TimeProjection:
    """
    Fixture to provide an instance of the TimeProjection class.
    """
    return TimeProjection()


@pytest.fixture
def equations() -> Equations:
    """
    Fixture to provide an instance of the Equations class.
    """
    return Equations()


@pytest.fixture
def bmr_model() -> RMRModel:
    """
    Fixture to provide an instance of the BMRModel class.
    """
    return RMRModel()


@pytest.fixture
def valid_input_data() -> dict:
    """
    Fixture to provide valid input data for tests.
    """
    return {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 70.0,
        "height": 175.0,
        "weight_loss_rate": 0.5,
        "duration": 10,
    }


@pytest.fixture
def invalid_age_data(valid_input_data):
    """
    Fixture to provide input data with invalid age.
    """
    data = valid_input_data.copy()
    data["age"] = 10  # Invalid age
    return data
