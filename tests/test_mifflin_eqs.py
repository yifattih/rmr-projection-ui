import unittest
import pytest
import numpy as np
from app.src.bmr.helpers.equations import Mifflin


class TestEquationsMifflin(unittest.TestCase):

###############################################################################
##                    Override method tests                                  ##
###############################################################################

    def test_equations_mifflin_str(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        weight_loss_rate = 2
        energy_deficit = 0
        sex = 'male'
        mifflin = Mifflin(
            age=age,
            height=height,
            weight=weight_initial,
            time_projection=time_projected,
            sex=sex,
            weight_loss_rate=weight_loss_rate,
            energy_deficit=energy_deficit
        )
        str_expected = (
            f"Mifflin-St. Jeor BMR equation for a {age}-years "
            f"old person with {weight_initial}-lbs weight and "
            f"{height}-inches height. Projection over "
            f"{time_projected}-weeks with a weight loss rate of "
            f"{weight_loss_rate}-lbs per week and an energy "
            f"deficit of {energy_deficit}-cals"
        )
        str_actual = str(mifflin)
        self.assertEqual(str_expected, str_actual)

    def test_equations_mifflin_repr(self) -> None:
        age = 22
        height = 5.5
        weight_initial = 10
        time_projected = np.array([1, 2, 3])
        units = "imperial"
        weight_loss_rate = 2
        energy_deficit = 0
        sex = 'male'
        mifflin = Mifflin(
            age=age,
            height=height,
            weight=weight_initial,
            time_projection=time_projected,
            sex=sex,
            weight_loss_rate=weight_loss_rate,
            energy_deficit=energy_deficit
        )
        repr_expected = (
            f"Mifflin-St. Jeor({age}, {height}, {weight_initial}, "
            f"{time_projected}, {weight_loss_rate}, "
            f"{energy_deficit}, {units})"
        )
        repr_actual = repr(mifflin)
        self.assertEqual(repr_expected, repr_actual)

###############################################################################
##                    Input validation tests                                 ##
###############################################################################

    def test_equations_mifflin_raises_assertion_age_less_19(
        self,
    ) -> None:
        age = 5
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = 0
        weight_loss_rate = 0.5
        sex = 'male'
        units = 'metric'
        with pytest.raises(AssertionError):
            Mifflin(
                age=age,
                height=height,
                weight=weight_initial,
                time_projection=time_projected,
                sex=sex,
                weight_loss_rate=weight_loss_rate,
                energy_deficit=energy_deficit
            )

    def test_equations_miffflin_raises_assertion_height_less_0(
        self,
    ) -> None:
        age = 22
        height = -10
        time_projected = np.array([1, 2, 3])
        weight_initial = np.array([100, 98, 88])
        energy_deficit = 0
        weight_loss_rate = 2
        sex = 'male'
        with pytest.raises(AssertionError):
            Mifflin(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,  # type: ignore
                weight_loss_rate=weight_loss_rate,
                energy_deficit=energy_deficit
            )

    def test_equations_mifflin_raises_assertion_time_empty(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([])
        weight_initial = np.array([100, 98, 88])
        energy_deficit = 0
        weight_loss_rate = 0.5
        sex = 'male'
        with pytest.raises(AssertionError):
            Mifflin(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,  # type: ignore
                weight_loss_rate=weight_loss_rate,
                energy_deficit=energy_deficit
            )

    def test_equations_mifflin_raises_assertion_weight_negative(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = -1
        energy_deficit = 0
        weight_loss_rate = 0.2
        sex = 'male'
        with pytest.raises(AssertionError):
            Mifflin(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,
                weight_loss_rate=weight_loss_rate,
                energy_deficit=energy_deficit
            )

    def test_equations_mifflin_raises_assertion_energy_deficit_negative(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = -10
        weight_loss_rate = 0.5
        sex = 'male'
        with pytest.raises(AssertionError):
                Mifflin(
                    age=age,
                    height=height,
                    time_projection=time_projected,
                    sex=sex,
                    weight=weight_initial,
                    weight_loss_rate=weight_loss_rate,
                    energy_deficit=energy_deficit
                    )
    
    def test_equations_mifflin_raises_assertion_sex_invalid(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = -10
        weight_loss_rate = 0.5
        sex = 'apple' # non mae or female valuess for sex
        with pytest.raises(AssertionError):
                Mifflin(
                    age=age,
                    height=height,
                    time_projection=time_projected,
                    sex=sex,
                    weight=weight_initial,
                    weight_loss_rate=weight_loss_rate,
                    energy_deficit=energy_deficit
                    )
                
    def test_equations_mifflin_raises_assertion_sex_empty(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = -10
        weight_loss_rate = 0.5
        sex = ''
        with pytest.raises(AssertionError):
                Mifflin(
                    age=age,
                    height=height,
                    time_projection=time_projected,
                    sex=sex,
                    weight=weight_initial,
                    weight_loss_rate=weight_loss_rate,
                    energy_deficit=energy_deficit
                    )

###############################################################################
##                   Correct calculation tests                               ##
##                                                                           ##
## For both men and women the following vallus will be tested:               ##
## Imperial:                                                                 ##
##       initial weight = 196 lb
##       height = 71 in
##       age = 33 yrs
##       energy deficit = 1000
##       time projection = 0
##       weight loss rate = 2
## 
## Metric:                                                                 ##
##       initial weight = 88.9 kg
##       height = 180.34 cm
##       age = 33 yrs
##       energy deficit = 1000
##       time projection = 0
##       weight loss rate = 0.5
###############################################################################

    def test_men_eq_imperial_return_valid_result(self) -> None:
        age = 33
        height = 71
        weight_initial = 196
        time_projected = np.array([0])
        weight_loss_rate = 2
        units = 'imperial'
        sex = 'male'
        mifflin = Mifflin(
            age=age,
            height=height,
            weight=weight_initial,
            time_projection=time_projected,
            sex=sex,
            weight_loss_rate=weight_loss_rate,
            units=units

        )
        bmr_expected, bmr_deficit_expected = (
            np.array([1856.18]),
            np.array([856.18]),
        )
        (bmr_actual, bmr_deficit_actual) = np.round(
            mifflin.get_bmr_and_deficit(), 2
        )
        for i in range(0, len(bmr_expected)):
            self.assertEqual(bmr_expected[i], bmr_actual[i])
            self.assertEqual(bmr_deficit_expected[i], bmr_deficit_actual[i])    

    def test_men_eq_metric_return_valid_result(self) -> None:
        age = 33
        height = 180.34
        weight_initial = 88.9
        time_projected = np.array([0])
        weight_loss_rate = 0.5
        units = 'metric'
        sex = 'male'
        mifflin = Mifflin(
            age=age,
            height=height,
            weight=weight_initial,
            time_projection=time_projected,
            sex=sex,
            weight_loss_rate=weight_loss_rate,
            units = units

        )
        bmr_expected, bmr_deficit_expected = (
            np.array([1856.12]),
            np.array([856.12]),
        )
        (bmr_actual, bmr_deficit_actual) = np.round(
            mifflin.get_bmr_and_deficit(), 2
        )
        for i in range(0, len(bmr_expected)):
            self.assertEqual(bmr_expected[i], bmr_actual[i])
            self.assertEqual(bmr_deficit_expected[i], bmr_deficit_actual[i])


    def test_women_eq_imperial_return_valid_result(self) -> None:
        age = 33
        height = 71
        weight_initial = 196
        time_projected = np.array([0])
        weight_loss_rate = 2
        units = 'imperial'
        sex = 'female'
        mifflin = Mifflin(
                age=age,
                height=height,
                weight=weight_initial,
                time_projection=time_projected,
                sex=sex,
                weight_loss_rate=weight_loss_rate,
                units=units

        )
        bmr_expected, bmr_deficit_expected = (
            np.array([1690.18]),
            np.array([690.18]),
        )

        (bmr_actual, bmr_deficit_actual) = np.round(
            mifflin.get_bmr_and_deficit(), 2
        )
        for i in range(0, len(bmr_expected)):
            self.assertEqual(bmr_expected[i], bmr_actual[i])
            self.assertEqual(bmr_deficit_expected[i], bmr_deficit_actual[i])    

    def test_women_eq_metric_return_valid_result(self) -> None:
        age = 33
        height = 180.34
        weight_initial = 88.9
        time_projected = np.array([0])
        weight_loss_rate = 0.5
        units = 'metric'
        sex = 'female'
        mifflin = Mifflin(
                age=age,
                height=height,
                weight=weight_initial,
                time_projection=time_projected,
                sex=sex,
                weight_loss_rate=weight_loss_rate,
                units=units

        )
        bmr_expected, bmr_deficit_expected = (
            np.array([1690.12]),
            np.array([690.12]),
        )
        (bmr_actual, bmr_deficit_actual) = np.round(
            mifflin.get_bmr_and_deficit(), 2
        )
        for i in range(0, len(bmr_expected)):
            self.assertEqual(bmr_expected[i], bmr_actual[i])
            self.assertEqual(bmr_deficit_expected[i], bmr_deficit_actual[i])


