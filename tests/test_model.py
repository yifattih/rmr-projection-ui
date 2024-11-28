import unittest
from app.src.bmr import model

class TestModel(unittest.TestCase):
    def test_model_mifflin_return_dict(self) -> None:
        data = {
            "age": 33,
            "height": 71,
            "weight": 196,
            "weeks": 0,
            "units": "imperial",
            "weight_loss_rate": 2,
            "energy_deficit": 1000,
            "sex": "male",
        }

        bmr_model = model.Builder(data=data)
        bmr_model.build()
        bmr_model.calculate(equation='Mifflin')

        results_expected = {
            "age": 33,
            "bmr": [1856.0],
            "bmr_deficit": [856.0],
            "energy_deficit": 1000,
            "height": 71,
            "sex": "male",
            "time_projected": [0],
            "units": "imperial",
            "weeks": 0,
            "weight": 196,
            "weight_loss_rate": 2,
            "weight_proj": [196],
        }

        results_actual = bmr_model.jasonable_dict()

        self.assertEqual(results_expected, results_actual)

    def test_model_harris_return_dict(self) -> None:
        data = {
            "age": 33,
            "height": 71,
            "weight": 196,
            "weeks": 0,
            "units": "imperial",
            "weight_loss_rate": 2,
            "energy_deficit": 1000,
            "sex": "male",
        }

        bmr_model = model.Builder(data=data)
        bmr_model.build()
        bmr_model.calculate(equation='HarrisBenedict')

        results_expected = {
            "age": 33,
            "bmr": [1968.0],
            "bmr_deficit": [968.0],
            "energy_deficit": 1000,
            "height": 71,
            "sex": "male",
            "time_projected": [0],
            "units": "imperial",
            "weeks": 0,
            "weight": 196,
            "weight_loss_rate": 2,
            "weight_proj": [196],
        }

        results_actual = bmr_model.jasonable_dict()

        self.assertEqual(results_expected, results_actual)


  



  




