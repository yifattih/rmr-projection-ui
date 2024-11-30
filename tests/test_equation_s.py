import unittest
import pytest
import numpy as np
from app.src.bmr.helpers.equation_s import mifflinStJeor


@pytest.fixture(scope="class")
def fixture_data(request) -> None:
    request.cls.data = {"sex": "male",
            "units": "imperial",
            "age": 33,
            "weight": 196,
            "height": 71,
            "wlr": 2,
            "time_projection": np.linspace(0, 10, 11, dtype=int),
            "weight_projection": np.linspace(196, 176, 11, dtype=int)}

@pytest.mark.usefixtures("fixture_data")
class TestEquation(unittest.TestCase):
    def test_mifflinStJeor__str__and__repr__(self) -> None:
        mifflin_stjoer = mifflinStJeor(data=self.data)
        expected = (f"Mifflin-St. Joer RMR equations for a "
                f"{self.data["age"]}-years old person with "
                f"{self.data["weight"]}-lbs weight and "
                f"{self.data["height"]}-in height. Projection "
                f"over ({len(self.data["time_projection"])}-weeks with a "
                f"weight loss rate of {self.data["wlr"]}-lbs "
                f"per week"
                )
        actual = str(mifflin_stjoer)
        self.assertEqual(expected, actual)
        expected = (f"mifflinStJeor({self.data["sex"]}, {self.data["units"]}, "
                    f"{self.data["age"]}, {self.data["weight"]}, "
                    f"{self.data["height"]}, {self.data["wlr"]}, "
                    f"{self.data["time_projection"]})"
                    )
        actual = repr(mifflin_stjoer)
        self.assertEqual(expected, actual)