from pydantic import BaseModel, Field, root_validator
import numpy as np


class IrisInput(BaseModel):
    sepal_length: float = Field(..., description="Length of the sepal in cm")
    sepal_width: float = Field(..., description="Width of the sepal in cm")
    petal_length: float = Field(..., description="Length of the petal in cm")
    petal_width: float = Field(..., description="Width of the petal in cm")

    # Root validator to convert the input data to a numpy array
    @root_validator(pre=True)
    def convert_to_numpy(cls, values):
        sepal_length = values.get('sepal_length')
        sepal_width = values.get('sepal_width')
        petal_length = values.get('petal_length')
        petal_width = values.get('petal_width')

        # Ensure the values are positive
        if sepal_length <= 0 or sepal_width <= 0 or petal_length <= 0 or petal_width <= 0:
            raise ValueError("All measurements must be positive values.")

        # Convert input to numpy array and add it to the model's values
        values['input_data'] = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        return values


class IrisPrediction(BaseModel):
    predicted_class: int = Field(..., description="Predicted class of the iris flower")
    predicted_class_name: str = Field(
        ..., description="Predicted class name (e.g., Setosa, Versicolor, Virginica)"
    )
