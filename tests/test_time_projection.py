import unittest
import pytest
import numpy as np
from app.src.bmr.helpers import time_projection


class TestTimeProjection(unittest.TestCase):
    def test_time_projection_return_np_array(self) -> None:
        weeks = 7
        time_projected_actual = time_projection.calculate(weeks=weeks)
        self.assertEqual(np.ndarray, type(time_projected_actual))

    def test_time_projection_return_valid_np_array(self) -> None:
        weeks = 7
        time_projected_expected = np.arange(0, weeks + 1, 1)
        time_projected_actual = time_projection.calculate(weeks=weeks)
        for i in range(0, len(time_projected_expected)):
            self.assertEqual(
                time_projected_expected[i], time_projected_actual[i]
            )

    def test_time_projection_raises_assertionerror(self) -> None:
        weeks = 100
        with pytest.raises(AssertionError):
            time_projection.calculate(weeks=weeks)
