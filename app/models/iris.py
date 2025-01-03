from pydantic import BaseModel, Field
from fastapi import Form

class IrisInput(BaseModel):
    sepal_length: float = Form(..., description="Length of the sepal in cm")
    sepal_width: float = Form(..., description="Width of the sepal in cm")
    petal_length: float = Form(..., description="Length of the petal in cm")
    petal_width: float = Form(..., description="Width of the petal in cm")

    class Config:
        orm_mode = True




class IrisPrediction(BaseModel):
    predicted_class: int = Field(..., description="Predicted class of the iris flower")
    predicted_class_name: str = Field(
        ..., description="Predicted class name"
    )
