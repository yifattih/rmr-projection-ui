import numpy as np


def calculate(
    weight_initial: int, time_projection: np.ndarray = np.arange(0, 8, 1)
) -> np.ndarray:
    try:
        assert weight_initial > 0
        return weight_initial - 2 * time_projection
    except AssertionError:
        raise AssertionError(
            f"{weight_initial}-lbs fall outside the allowed "
            f"range (0, \u221E)"
        )
