from fastapi import FastAPI, HTTPException
from utils.models import PredictionInput
from utils.schemas import PredictionData
from predictor import IrisModelHandler
from utils.configs import MODEL_PATH, TARGET_NAMES

app = FastAPI()


@app.get("/")
def root():
    return {"message": "hello world"}


@app.post("/predict", response_model=PredictionData)
def predict(data: PredictionInput):
    try:
        # Convert input data to numpy format
        input_data = data.to_numpy()

        # Initialize the IrisModelHandler with required arguments
        model_obj = IrisModelHandler(model_path=MODEL_PATH)

        # Load the pre-trained model
        model_obj.load_model()

        # Perform the prediction
        prediction_label, prediction_name = model_obj.predict(input_data)

        # Return the prediction as per the PredictionData schema
        return PredictionData(
            prediction_label=prediction_label,
            prediction_name=prediction_name
        )


    except Exception as e:
        # Log the exception and raise an HTTPException with a proper error message
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
