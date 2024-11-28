import numpy as np
from typing import TypeAlias
from app.src.bmr.helpers import time_projection as time_proj
from app.src.bmr.helpers import weight_projection as weight_proj
from app.src.bmr.helpers.equations import HarrisBenedict, Mifflin

JSONType: TypeAlias = dict[str, str | None]


class Builder:
    def __init__(self, data: JSONType) -> None:
        """Constructor"""
        self.age = data["age"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.weeks = data["weeks"]
        self.units = data["units"]
        self.weight_loss_rate = data["weight_loss_rate"]
        self.energy_deficit = data["energy_deficit"]
        self.sex = data["sex"]
        self.time_proj = time_proj.calculate(weeks=self.weeks)
        self.weight_proj = weight_proj.calculate(
            weight_initial=self.weight, time_projection=self.time_proj
        )
        self.equations = {} # JD - new empty dictionary to hold equation objects

    def build(self) -> Exception | None:

        # here, both equations are stored in a dictionary so that either can be
        # chosen downstream by using the equation keyword.
        # valid kewords:
        #       "HarrisBenedict" - Haris Benedict equation
        #       "Mifflin" - Mifflin-St. Jeor equation
    
         
        try:
            self.equations["HarrisBenedict"] = HarrisBenedict(
                age=self.age,
                height=self.height,
                weight=self.weight,
                time_projection=self.time_proj,
                sex=self.sex,
                units=self.units,
                weight_loss_rate=self.weight_loss_rate,
                energy_deficit=self.energy_deficit,
            )

            self.equations["Mifflin"] = Mifflin(
                age=self.age,
                height=self.height,
                weight=self.weight,
                time_projection=self.time_proj,
                sex=self.sex,
                units=self.units,
                weight_loss_rate=self.weight_loss_rate,
                energy_deficit=self.energy_deficit,
            )
        except Exception as e:
            return e

    def calculate(self, equation='Mifflin') -> None:
        '''
        Perform BMR calculation with selected equation.
        Defaults to HarrisBenedict equation.
        '''

        # Choice of equation must match implemented equation classes
        assert equation in self.equations.keys(), (
            f"Unknown equation: {equation}"
            f"Valid equations: {self.equations.keys()}"
        )
        
        self.bmr, self.bmr_deficit = self.equations[equation].get_bmr_and_deficit()

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
