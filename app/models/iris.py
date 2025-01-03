from pydantic import BaseModel, Field


class IrisInput(BaseModel):
    sepal_length: float = Field(..., description="Length of the sepal in cm")
    sepal_width: float = Field(..., description="Width of the sepal in cm")
    petal_length: float = Field(..., description="Length of the petal in cm")
    petal_width: float = Field(..., description="Width of the petal in cm")


class IrisPrediction(BaseModel):
    predicted_class: int = Field(..., description="Predicted class of the iris flower")
    predicted_class_name: str = Field(
        ..., description="Predicted class name (e.g., Setosa, Versicolor, Virginica)"
    )
