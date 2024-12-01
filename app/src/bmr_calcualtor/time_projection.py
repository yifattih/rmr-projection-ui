import numpy as np


class TimeProjection:
    """
    Helper class to generate a time projection array.

    Methods
    -------
    calculate(end: int) -> dict
        Generates a NumPy array from 0 to `end`, inclusive.
    """

    def calculate(self, end: int) -> dict:
        """
        Generates a time projection array from 0 to `end`.

        Parameters
        ----------
        end : int
            The endpoint of the time projection array. Must be non-negative.

        Returns
        -------
        dict
            A dictionary with the following structure:
            - "result" : numpy.ndarray
                The time projection array (if successful).
            - "error" : str, optional
                The error message (if failed).
            - "exit_code" : int
                0 if successful, 1 if an error occurred.
        """
        try:
            if end < 0:
                raise ValueError("Duration must be non-negative.")
            return {"result": np.arange(0, end + 1), "exit_code": 0}
        except Exception as e:
            return {"error": str(e), "exit_code": 1}
