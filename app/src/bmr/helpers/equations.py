import numpy as np


class HarrisBenedict:
    def __init__(
        self,
        age: int,
        height: float,
        weight: float,
        time_projection: np.ndarray,
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

    def men_eq(self) -> tuple[np.ndarray, np.ndarray]:
        if self.units == "imperial":
            bmr = (
                66.47
                + 6.24
                * (
                    self.weight
                    - (self.weight_loss_rate * self.time_projection)
                )
                + 12.7 * self.height
                - 6.76 * self.age
            )
            bmr_deficit = bmr - self.energy_deficit
            return bmr, bmr_deficit
        else:
            bmr = (
                66.5
                + 13.75
                * (self.weight - self.weight_loss_rate * self.time_projection)
                + 5.003 * self.height
                - 6.75 * self.age
            )
            bmr_deficit = bmr - self.energy_deficit
            return bmr, bmr_deficit

    def female_eq(self) -> tuple[np.ndarray, np.ndarray]:
        if self.units == "imperial":
            bmr = (
                65.51
                + 4.34
                * (
                    self.weight
                    - (self.weight_loss_rate * self.time_projection)
                )
                + 4.7 * (self.height)
                - 4.7 * (self.age)
            )
            bmr_deficit = bmr - self.energy_deficit
            return bmr, bmr_deficit
        else:
            bmr = (
                655.1
                + 9.563
                * (self.weight - self.weight_loss_rate * self.time_projection)
                + 1.850 * self.height
                - 4.676 * self.age
            )
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
