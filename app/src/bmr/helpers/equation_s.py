from app.src.bmr.helpers.coefficients import MIFFLINSTJEOR

class mifflinStJeor:
    """
    Mifflin-St.Jeor RMR equations
    ----------
    This class will calculat the RMR using the Mifflin-St. Jeor
    equations defined below:

    For male:
        SI units system:
            BMR = 10*weight[kg] + 6.25*height[cm] - 5*age[years] + 5
        Imperial units system:
            BMR = 4.536*weight[lbs] + 15.875*height[inches] − 5*age[years] + 5
    For female:
        SI units system:
            BMR = 10*weight[kg] + 6.25*height[cm] - 5*age[years] - 161
        Imperial units system:
            BMR = 4.536*weight[lbs] + 15.875*height[inches] − 5*age[years] 
            − 161;

    Parameters
    ----------
    data : dict
        {"units": "imperial" | "si",
        "sex": "male" | "female",
        "age": int,
        "weight": int,
        "height": int | float,
        "wlr": float,
        "time": np.ndarray}

    Attributes
    ----------
    data : int
        {"units": "imperial" | "si",
        "sex": "male" | "female",
        "age": int,
        "weight": int,
        "height": int | float,
        "wlr": float,
        "time": np.ndarray}
    coefficients : str
        Equations coefficients loaded from coefficients.py module:
            MIFFLINSTJEOIR = {<sex>: {<units>: {<coefficient name>: value}}}

    Methods
    ----------
    calculatermr()
        Calculates the Resting Metabolic Rate.

    Examples
    ----------
    >>> mifflin_stjeor = mifflinStJeor(data)
    >>> mifflin_stjeor.calculatermr()

    """
    def __init__(self, data: dict) -> None:
        """
        Mifflin-St.Jeor RMR constructor
        ----------

        Parameters
        ----------
        data : dict
            {"units": "imperial" | "si",
            "sex": "male" | "female",
            "age": int,
            "weight": int,
            "height": int | float,
            "wlr": float,
            "time": np.ndarray}

        Returns
        -------
        None

        Raises
        ------
        None
        """
        
        self.data = data
        self.coefficients = MIFFLINSTJEOR[self.data["sex"]][self.data["units"]]

        ############################################
            # For class string representations #
        ############################################
        if data["units"] == "imperial":
            self.height_unit = "in"
            self.weight_unit = "lbs"
        else:
            self.height_unit = "m"
            self.weight_unit = "kg"

    def __str__(self) -> str:
        """
        Class Redable Representation
        ----------

        Displays a summary of the class and its parameters.

        Returns:
            str: The string representation.
        """
        return (f"Mifflin-St. Joer RMR equations for a "
                f"{self.data["age"]}-years old person with "
                f"{self.data["weight"]}-{self.weight_unit} weight and "
                f"{self.data["height"]}-{self.height_unit} height. Projection "
                f"over ({len(self.data["time_projection"])}-weeks with a "
                f"weight loss rate of {self.data["wlr"]}-{self.weight_unit} "
                f"per week"
                )
    
    def calculatermr(self) -> dict:
        age = self.data["age"]
        weight = self.data["weight"]
        height = self.data["height"]
        weight_loss_rate = self.data["wlr"]
        time_projection = self.data["time_projection"]
        weight_coeff = self.coefficients['weight']
        h_coeff = self.coefficients['height']
        age_coeff = self.coefficients['age']
        bias = self.coefficients['bias']
        rmr = ((weight_coeff * (weight - (weight_loss_rate * time_projection)))
               + (h_coeff * height)
               + (age_coeff * age)
               + bias
               )
        return rmr

    def __repr__(self) -> str:
        """
        Class Repeatable Representation
        ----------

        Displays how to construct the class with provided parameters.

        Returns:
            str: The string representation.
        """
        return (f"mifflinStJeor({self.data["sex"]}, {self.data["units"]}, "
                f"{self.data["age"]}, {self.data["weight"]}, "
                f"{self.data["height"]}, {self.data["wlr"]}, "
                f"{self.data["time_projection"]})"
                )