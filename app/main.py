from fastapi import FastAPI
import numpy as np
from app.models.iris import IrisInput, IrisPrediction
from app.processors.model_processor import ModelProcessor


app = FastAPI()

# Initialize the model processor
model_processor = ModelProcessor()


@app.get("/", response_model=str)
async def read_root():
    return "Welcome :)"


@app.post("/predict", response_model=IrisPrediction)
async def predict(data: IrisInput):
    # Convert the input data to a numpy array
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])

    # Make a prediction using the model processor
    predicted_class = model_processor.predict(input_data)
    predicted_class_name = model_processor.get_class_name(predicted_class)

    # Return the prediction result in JSON format
    return IrisPrediction(
        predicted_class=predicted_class, predicted_class_name=predicted_class_name
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
