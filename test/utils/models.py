from pydantic import BaseModel, Field, validator
import numpy as np

class PredictionInput(BaseModel):
    sepal_length: float = Field(..., description="Sepal length must be positive")
    sepal_width: float = Field(..., description="Sepal width must be positive")
    petal_length: float = Field(..., description="Petal length must be positive")
    petal_width: float = Field(..., description="Petal width must be positive")

    @validator("*", pre=True)
    def check_non_negative(cls, value):
        if value <= 0:
            raise ValueError("All measurements must be positive.")
        return value

    def to_numpy(self):
        return np.array([list(self.model_dump().values())])


