import numpy as np
from coefficients import MIFFLINSTJEOR


class Equations:
    """
    Helper class to calculate the resting metabolic rate (RMR).

    Methods
    -------
    mifflinstjeor_rmr(sex, units, age, weight, height, weight_loss_rate,
    time_projection) -> dict
        Calculates RMR over a given time projection using the Mifflin-St. Jeor
        equations.
    """

    def mifflinstjeor_rmr(
        self,
        sex: str,
        units: str,
        age: int,
        weight: float,
        height: float,
        weight_loss_rate: float,
        time_projection: np.ndarray,
    ) -> dict:
        """
        Calculates RMR over a time projection using the Mifflin-St Jeor
        equations.

        Parameters
        ----------
        sex : str
            The sex of the individual ("male" or "female").
        units : str
            The units system ("si" or "imperial").
        age : int
            The age of the individual in years.
        weight : float
            The weight of the individual in kilograms (si) or pounds
            (imperial).
        height : float
            The height of the individual in meters (si) or inches (imperial).
        weight_loss_rate : float
            The rate of weight loss per time unit.
        time_projection : numpy.ndarray
            A NumPy array representing the time projection.

        Returns
        -------
        dict
            A dictionary with the following structure:
            - "result" : numpy.ndarray
                The calculated RMR values over time (if successful).
            - "error" : str, optional
                The error message (if failed).
            - "exit_code" : int
                0 if successful, 1 if an error occurred.
        """
        try:
            coeffs = MIFFLINSTJEOR[sex][units]
            weight_coeff = coeffs["weight"]
            height_coeff = coeffs["height"]
            age_coeff = coeffs["age"]
            bias = coeffs["bias"]

            rmr = (
                weight_coeff * (weight - weight_loss_rate * time_projection)
                + height_coeff * height
                + age_coeff * age
                + bias
            )
            return {"result": rmr, "exit_code": 0}
        except KeyError as e:
            return {
                "error": f"Invalid combination of sex or units: {e}",
                "exit_code": 1,
            }
        except Exception as e:
            return {"error": str(e), "exit_code": 1}
