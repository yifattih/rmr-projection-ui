import numpy as np
from app.src.bmr.helpers.coefficients import coefficients

class HarrisBenedict:
    def __init__(
        self,
        age: int,
        height: float,
        weight: float,
        time_projection: np.ndarray,
        sex: str,
        units: str = "imperial",
        weight_loss_rate: float = 2,
        energy_deficit: float = 1000,
    ) -> None:

        assert 19 <= age <= 150, (
            "Height stop chaning probalbly after 19"
            "and normally people don't live more than "
            "150 year!"
        )
        assert height >= 0, "Height must be positive"
        assert time_projection.size != 0, (
            "Time projection is required. "
            "Calculate with the "
            "time_projection module"
        )
        assert weight >= 0, "Initial weight must be positive"
        assert energy_deficit >= 0, "Energy deficit must be positive"
        assert units == "imperial" or units == "metric", (
            "Units must be on " "imperial or metric" "system"
        )

        if units == "imperial":
            self.height_unit = "inches"
            self.weight_unit = "lbs"
        else:
            self.height_unit = "cm"
            self.weight_unit = "kg"

        self.age = age
        self.height = height
        self.time_projection = time_projection
        self.weight = weight
        self.weight_loss_rate = weight_loss_rate
        self.energy_deficit = energy_deficit
        self.units = units
        self.sex = sex

        self.coefficients = coefficients['HarrisBenedict'][self.sex][self.units]
        # make sure the coefficients are loaded
        assert self.coefficients != None

    def get_bmr(self) -> float:
        bmr = (
            (self.coefficients['weight'] * (self.weight - (self.weight_loss_rate * self.time_projection)))
            + (self.coefficients['height'] * self.height)
            + (self.coefficients['age'] * self.age)
            + self.coefficients['bias']
            )
        return bmr
    
    def get_bmr_and_deficit(self) -> tuple[np.array, np.array]:
        bmr = self.get_bmr()
        bmr_deficit = bmr - self.energy_deficit
        return bmr, bmr_deficit

    def __str__(self) -> str:
        return (
            f"Harris-Benedict BMR equations for a {self.age}-years "
            f"old person with {self.weight}-{self.weight_unit} weight and "
            f"{self.height}-{self.height_unit} height. Projection over "
            f"{self.time_projection}-weeks with a weight loss rate of "
            f"{self.weight_loss_rate}-{self.weight_unit} per week and "
            f"an energy deficit of {self.energy_deficit}-cals"
        )

    def __repr__(self) -> str:
        return (
            f"HarrisBenedict({self.age}, {self.height}, "
            f"{self.weight}, {self.time_projection}, "
            f"{self.weight_loss_rate}, {self.energy_deficit}, "
            f"{self.units})"
        )


class Mifflin:
    """Mifflin-St.Jeor bmr equation
    This class will calculat the BMR using the Mifflin-St. Jeor
    equation defined below:
    for men:
        metric
        BMR = 10*weight[kg] + 6.25*height[cm] - 5*age[years] + 5
        imperial
        BMR = 4.536*weight[lbs] + 15.875*height[inches] − 5*age[years] + 5
    for women:
        metric
        BMR = 10*weight[kg] + 6.25*height[cm] - 5*age[years] - 161
        imperial
        BMR = 4.536*weight[lbs] + 15.875*height[inches] − 5*age[years] − 161;
    """

    def __init__(
        self,
        age: int,
        height: float,
        weight: float,
        time_projection: np.ndarray,
        sex: str,
        units: str = "imperial",
        weight_loss_rate: float = 2,
        energy_deficit: float = 1000,
    ) -> None:

        assert 19 <= age <= 150, (
            "Height stop chaning probalbly after 19"
            "and normally people don't live more than "
            "150 years!"
        )
        assert height >= 0, "Height must be positive"
        assert time_projection.size != 0, (
            "Time projection is required. "
            "Calculate with the "
            "time_projection module"
        )
        assert weight >= 0, "Initial weight must be positive"
        assert energy_deficit >= 0, "Energy deficit must be positive"
        assert units == "imperial" or units == "metric", (
            "Units must be on " "imperial or metric" "system"
        )

        assert sex in ['male', 'female'], ('Sex must be male or female')

        if units == "imperial":
            self.height_unit = "inches"
            self.weight_unit = "lbs"
        else:
            self.height_unit = "cm"
            self.weight_unit = "kg"
        

        self.age = age
        self.height = height
        self.time_projection = time_projection
        self.weight = weight
        self.energy_deficit = energy_deficit
        self.units = units
        self.weight_loss_rate = weight_loss_rate
        self.sex = sex

        self.coefficients = coefficients['Mifflin'][self.sex][self.units]
        # make sure the coefficients are loaded
        assert self.coefficients != None

    def get_bmr(self) -> float:
        bmr = (
            (self.coefficients['weight'] * (self.weight - (self.weight_loss_rate * self.time_projection)))
            + (self.coefficients['height'] * self.height)
            + (self.coefficients['age'] * self.age)
            + self.coefficients['bias']
            )
        return bmr
    
    def get_bmr_and_deficit(self) -> tuple[np.ndarray, np.ndarray]:
        bmr = self.get_bmr()
        bmr_deficit = bmr - self.energy_deficit
        return bmr, bmr_deficit
    
    def __str__(self) -> str:
        return (
            f"Mifflin-St. Jeor BMR equation for a {self.age}-years "
            f"old person with {self.weight}-{self.weight_unit} weight and "
            f"{self.height}-{self.height_unit} height. Projection over "
            f"{self.time_projection}-weeks with a weight loss rate of "
            f"{self.weight_loss_rate}-{self.weight_unit} per week and "
            f"an energy deficit of {self.energy_deficit}-cals"
        )

    def __repr__(self) -> str:
        return (
            f"Mifflin-St. Jeor({self.age}, {self.height}, "
            f"{self.weight}, {self.time_projection}, "
            f"{self.weight_loss_rate}, {self.energy_deficit}, "
            f"{self.units})"
        )
