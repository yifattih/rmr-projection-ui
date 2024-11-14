import unittest
import pytest
import numpy as np
from app.src.bmr.helpers import time_projection
from app.src.bmr.helpers import weight_projection


class TestWeightProjection(unittest.TestCase):
    def test_weight_projection_return_np_array(self) -> None:
        weight_initial = 100
        weight_projected_actual = weight_projection.calculate(
            weight_initial=weight_initial
        )
        self.assertEqual(np.ndarray, type(weight_projected_actual))

    def test_weight_projection_return_valid_np_array(self) -> None:
        weight_initial = 196
        weeks = 7
        time_projected = time_projection.calculate(weeks=weeks)
        weight_projected_expected = np.arange(
            weight_initial - 2 * weeks, weight_initial + 2, 2
        )[::-1]
        weight_projected_actual = weight_projection.calculate(
            weight_initial=weight_initial, time_projection=time_projected
        )
        for i in range(0, len(weight_projected_expected), 1):
            self.assertEqual(
                weight_projected_expected[i], weight_projected_actual[i]
            )

    def test_weight_projection_raises_assertionerror(self) -> None:
        weight_initial = -1
        with pytest.raises(AssertionError):
            weight_projection.calculate(weight_initial=weight_initial)
