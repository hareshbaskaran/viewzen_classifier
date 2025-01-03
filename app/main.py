from fastapi import FastAPI, Form
from pydantic import BaseModel
import numpy as np
from models.iris import IrisInput, IrisPrediction
from processors.model_processor import ModelProcessor

# Initialize FastAPI app
app = FastAPI()

# Initialize the model processor
model_processor = ModelProcessor()

@app.get("/", response_model=str)
async def read_root():
    return "Welcome to the Iris Prediction API!"

@app.post("/predict", response_model=IrisPrediction)
async def predict(
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...),
):
    # Convert the input data to a numpy array
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make a prediction using the model processor
    predicted_class = model_processor.predict(input_data)
    predicted_class_name = model_processor.get_class_name(predicted_class)

    # Return the prediction result in JSON format
    return IrisPrediction(predicted_class=predicted_class, predicted_class_name=predicted_class_name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
