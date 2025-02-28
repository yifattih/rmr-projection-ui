from typing import Dict, List, Literal
from pydantic import BaseModel, Field

class InputData(BaseModel):
    sex: Literal["male", "female"] = Field(
        description="The sex of the individual ('male' or 'female')"
    )
    units: Literal["si", "imperial"] = Field(
        description="The units system ('si' or 'imperial')"
    )
    age: int = Field(
        gt=19,
        le=150,
        description="Age of the individual in years (20 to 150)",
    )
    weight: float = Field(
        gt=1, description="Weight in kilograms (SI) or pounds (imperial)"
    )
    height: float = Field(
        gt=1, description="Height in meters (SI) or inches (imperial)"
    )
    weight_loss_rate: float = Field(
        ge=0, description="Rate of weight loss per time unit"
    )
    duration: int = Field(
        ge=0, description="Duration for the time projection (>= 0)"
    )

class OutputData(InputData):
    rmr: Dict[str, list] = Field(
        description="Resting Metabolic Rate (RMR) over the time projection"
    )
    time_projection: List[int] = Field(description="Time projection in weeks")