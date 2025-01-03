from pydantic import BaseModel, Field
class PredictionData(BaseModel):
    predicted_label: int = Field(..., description= "Predicted class label")
    predicted_name: str = Field(..., description= "Name of the predicted class label")