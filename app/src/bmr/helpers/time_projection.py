import numpy as np


def calculate(weeks: int = 7) -> np.ndarray:
    """
    Calculate a time projection in weeks with maximum value defined
    by input weeks parameter

    :param time: max value for time projection
    :type time: int, default = 7

    :return: weeks time projection
    :rtype: dict[str, str | np.ndarray]

    :raises: AssertionError: When input parameter is outside [0, 52]
    """
    try:
        assert 0 <= weeks <= 52
        time_projection = np.arange(0, weeks + 1, 1)
        return time_projection
    except AssertionError:
        raise AssertionError(
            f"{weeks}-weeks falls outside the allowed " f"range [0, 52]"
        )
