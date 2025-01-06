from pydantic import BaseModel, Field
class IrisInput(BaseModel):
    sepal_length: float = Field(..., description="Length of the sepal")
    sepal_width: float = Field(..., description="Width of the sepal")
    petal_length: float = Field(..., description="Length of the petal")
    petal_width: float = Field(..., description="Width of the Petal")


class IrisPrediction(BaseModel):
    predicted_class: int = Field(..., description="Predicted class of the iris flower")
    predicted_class_name: str = Field(
        ..., description="Predicted class name"
    )
