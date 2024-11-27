import numpy as np
from typing import TypeAlias
from .helpers import time_projection as time_proj
from .helpers import weight_projection as weight_proj
from .helpers.equations import HarrisBenedict

JSONType: TypeAlias = dict[str, str | None]


class Builder:
    def __init__(self, data: JSONType) -> None:
        """Constructor"""
        self.age = data["age"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.weeks = data["time"]
        self.units = data["units"]
        self.weight_loss_rate = data["rate"]
        self.energy_deficit = 1000
        self.sex = data["sex"]
        self.time_proj = time_proj.calculate(weeks=self.weeks)
        self.weight_proj = weight_proj.calculate(
            weight_initial=self.weight, time_projection=self.time_proj
        )

    def build(self) -> Exception | None:
        try:
            self.equations = HarrisBenedict(
                age=self.age,
                height=self.height,
                weight=self.weight,
                time_projection=self.time_proj,
                units=self.units,
                weight_loss_rate=self.weight_loss_rate,
                energy_deficit=self.energy_deficit,
            )
        except Exception as e:
            return e

    def calculate(self) -> None:
        if self.sex == "men":
            self.bmr, self.bmr_deficit = self.equations.men_eq()
        else:
            self.bmr, self.bmr_deficit = self.equations.female_eq()

    def jasonable_dict(self) -> dict:
        return {
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "weeks": self.weeks,
            "units": self.units,
            "weight_loss_rate": self.weight_loss_rate,
            "energy_deficit": self.energy_deficit,
            "sex": self.sex,
            "time_projected": self.time_proj.tolist(),
            "weight_proj": self.weight_proj.tolist(),
            "bmr": np.round(self.bmr, 0).tolist(),
            "bmr_deficit": np.round(self.bmr_deficit, 0).tolist(),
        }
