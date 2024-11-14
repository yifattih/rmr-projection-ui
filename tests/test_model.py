import unittest
from app.src.bmr import model


class TestModel(unittest.TestCase):
    def test_model_return_dict(self) -> None:
        data = {
            "age": 33,
            "height": 71,
            "weight": 196,
            "weeks": 0,
            "units": "imperial",
            "weight_loss_rate": 2,
            "energy_deficit": 1000,
            "sex": "men",
        }

        bmr_model = model.Builder(data=data)
        bmr_model.build()
        bmr_model.calculate()

        results_expected = {
            "age": 33,
            "bmr": [1968],
            "bmr_deficit": [968],
            "energy_deficit": 1000,
            "height": 71,
            "sex": "men",
            "time_projected": [0],
            "units": "imperial",
            "weeks": 0,
            "weight": 196,
            "weight_loss_rate": 2,
            "weight_proj": [196],
        }

        results_actual = bmr_model.jasonable_dict()

        self.assertEqual(results_expected, results_actual)
