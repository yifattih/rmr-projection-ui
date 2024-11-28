import unittest
import pytest
import numpy as np
from app.src.bmr.helpers.equations import HarrisBenedict


class TestEquationsHarrisBenedict(unittest.TestCase):
    def test_equations_harrisbenedict_str(self) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        weight_loss_rate = 2
        energy_deficit = 0
        sex = 'male'
        harris_benedict = HarrisBenedict(
            age=age,
            height=height,
            time_projection=time_projected,
            sex=sex,
            weight=weight_initial,
            energy_deficit=energy_deficit,
        )
        str_expected = (
            f"Harris-Benedict BMR equations for a {age}-years "
            f"old person with {weight_initial}-lbs weight and "
            f"{height}-inches height. Projection over "
            f"{time_projected}-weeks with a weight loss rate of "
            f"{weight_loss_rate}-lbs per week and an energy "
            f"deficit of {energy_deficit}-cals"
        )
        str_actual = str(harris_benedict)
        self.assertEqual(str_expected, str_actual)

    def test_equations_harrisbenedict_repr(self) -> None:
        age = 22
        height = 5.5
        weight_initial = 10
        time_projected = np.array([1, 2, 3])
        units = "imperial"
        weight_loss_rate = 2
        energy_deficit = 0
        sex='male'
        harris_benedict = HarrisBenedict(
            age=age,
            height=height,
            time_projection=time_projected,
            sex=sex,
            units="imperial",
            weight=weight_initial,
            energy_deficit=energy_deficit,
        )
        repr_expected = (
            f"HarrisBenedict({age}, {height}, {weight_initial}, "
            f"{time_projected}, {weight_loss_rate}, "
            f"{energy_deficit}, {units})"
        )
        repr_actual = repr(harris_benedict)
        self.assertEqual(repr_expected, repr_actual)

    def test_equations_harrisbenedict_raises_assertion_age_less_19(
        self,
    ) -> None:
        age = 5
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = 0
        sex='male'
        with pytest.raises(AssertionError):
            HarrisBenedict(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,
                energy_deficit=energy_deficit,
            )

    def test_equations_harrisbenedict_raises_assertion_height_less_0(
        self,
    ) -> None:
        age = 22
        height = -10
        time_projected = np.array([1, 2, 3])
        weight_initial = np.array([100, 98, 88])
        energy_deficit = 0
        sex = 'male'
        with pytest.raises(AssertionError):
            HarrisBenedict(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,  # type: ignore
                energy_deficit=energy_deficit,
            )

    def test_equations_harrisbenedict_raises_assertion_time_empty(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([])
        weight_initial = np.array([100, 98, 88])
        energy_deficit = 0
        sex = 'male'
        with pytest.raises(AssertionError):
            HarrisBenedict(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,  # type: ignore
                energy_deficit=energy_deficit,
            )

    def test_equations_harrisbenedict_raises_assertion_weight_negative(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = -1
        energy_deficit = 0
        sex = 'male'
        with pytest.raises(AssertionError):
            HarrisBenedict(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,
                energy_deficit=energy_deficit,
            )

    def test_equations_harrisbenedict_raises_assertion_energy_deficit_negative(
        self,
    ) -> None:
        age = 22
        height = 5.5
        time_projected = np.array([1, 2, 3])
        weight_initial = 10
        energy_deficit = -10
        sex = 'male'
        with pytest.raises(AssertionError):
            HarrisBenedict(
                age=age,
                height=height,
                time_projection=time_projected,
                sex=sex,
                weight=weight_initial,
                energy_deficit=energy_deficit,
            )

    def test_male_imperial_return_valid_result(self) -> None:
        age = 33
        height = 71
        weight_initial = 196
        time_projected = np.array([0])
        sex = 'male'
        harris_benedict = HarrisBenedict(
            age=age,
            height=height,
            weight=weight_initial,
            time_projection=time_projected,
            sex=sex
        )
        bmr_expected, bmr_deficit_expected = (
            np.array([1968.46]),
            np.array([968.46])
        )
        (bmr_actual, bmr_deficit_actual) = np.round(
            harris_benedict.get_bmr_and_deficit(), 2
        )

        for i in range(0, len(bmr_expected)):
            self.assertEqual(bmr_expected[i], bmr_actual[i])
            self.assertEqual(bmr_deficit_expected[i], bmr_deficit_actual[i])
