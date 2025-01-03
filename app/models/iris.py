from pydantic import BaseModel, Field
from fastapi import Form

class IrisInput(BaseModel):
    sepal_length: float = Form(...)
    sepal_width: float = Form(...)
    petal_length: float = Form(...)
    petal_width: float = Form(...)




class IrisPrediction(BaseModel):
    predicted_class: int = Field(..., description="Predicted class of the iris flower")
    predicted_class_name: str = Field(
        ..., description="Predicted class name"
    )
