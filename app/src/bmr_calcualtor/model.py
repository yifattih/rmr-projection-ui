from time_projection import TimeProjection
from equations import Equations


class RMRModel:
    """
    High-level model to process RMR calculations.

    This class validates input data, integrates helper modules, and provides
    error handling and detailed messages for both validation and helper module
    errors.

    Methods
    -------
    process(input_data: dict) -> dict
        Validates input data and calculates RMR over a time projection.
    """

    def __init__(self) -> None:
        """
        Initializes the RMRModel class with helper modules.
        """
        self.time_projection_helper = TimeProjection()
        self.equation_helper = Equations()

    def process(self, input_data: dict) -> dict:
        """
        Validates input data and calculates RMR over a time projection.

        Parameters
        ----------
        input_data : dict
            A dictionary containing the following keys:
            - "sex" : str
                The sex at birth of the individual ("male" or "female").
            - "units" : str
                The units system ("si" or "imperial").
            - "age" : int
                The age of the individual in years (> 20).
            - "weight" : float
                The weight of the individual in kilograms (si) or pounds
                (imperial) (> 0).
            - "height" : float
                The height of the individual in centimeters (si) or inches
                (imperial) (> 0).
            - "weight_loss_rate" : float
                The rate of weight loss per time unit (> 0).
            - "duration" : int
                The duration for the time projection (> 0).

        Returns
        -------
        dict
            A dictionary with the following structure:
            - "input" : dict, optional
                The original input data (if successful).
            - "output" : dict, optional
                The calculated RMR values and related outputs (if successful).
            - "error" : str, optional
                The error message (if failed).
            - "exit_code" : int
                0 if successful, 1 if an error occurred.
        """
        try:
            # Validate input presence
            required_keys = [
                "sex",
                "units",
                "age",
                "weight",
                "height",
                "weight_loss_rate",
                "duration",
            ]
            missing_keys = [
                key for key in required_keys if key not in input_data
            ]
            if missing_keys:
                return {
                    "error": f"Missing required keys: {missing_keys}",
                    "exit_code": 1,
                }

            # Extract inputs
            sex = input_data["sex"]
            units = input_data["units"]
            age = input_data["age"]
            weight = input_data["weight"]
            height = input_data["height"]
            weight_loss_rate = input_data["weight_loss_rate"]
            duration = input_data["duration"]

            # Validate values
            if not (19 < age <= 150):
                return {
                    "error": f"Invalid age: {age}. Age must be between \
                        20 and 150.",
                    "exit_code": 1,
                }
            if weight < 1:
                return {
                    "error": f"Invalid weight: {weight}. Weight must be \
                        greater than or equal to 1.",
                    "exit_code": 1,
                }
            if height < 1:
                return {
                    "error": f"Invalid height: {height}. Height must be \
                        greater than or equal to 1.",
                    "exit_code": 1,
                }
            if weight_loss_rate < 0:
                return {
                    "error": f"Invalid weight loss rate: {weight_loss_rate}.\
                        Weight loss rate must be non-negative.",
                    "exit_code": 1,
                }
            if duration < 0:
                return {
                    "error": f"Invalid duration: {duration}. Duration must be \
                        non-negative.",
                    "exit_code": 1,
                }

            # Step 1: Generate time projection
            time_result = self.time_projection_helper.calculate(duration)
            if time_result["exit_code"] != 0:
                return {
                    "error": f"Time projection failed: {time_result['error']}",
                    "exit_code": 1,
                }

            time_projection = time_result["result"]

            # Step 2: Calculate RMR
            rmr_result = self.equation_helper.mifflinstjeor_rmr(
                sex,
                units,
                age,
                weight,
                height,
                weight_loss_rate,
                time_projection,
            )
            if rmr_result["exit_code"] != 0:
                return {
                    "error": f"RMR calculation failed: {rmr_result['error']}",
                    "exit_code": 1,
                }

            # Return success response
            return {
                "input": input_data,
                "output": {"rmr": rmr_result["result"].tolist()},
                "exit_code": 0,
            }
        except Exception as e:
            return {"error": str(e), "exit_code": 1}
