from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.iris import IrisInput, IrisPrediction
from app.processors.model_processor import ModelProcessor
from app.utils.helpers import convert_model_to_numpy

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_processor = ModelProcessor()


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=IrisPrediction)
async def predict(data: IrisInput):
    # Convert the Pydantic model instance to numpy array
    input_data = convert_model_to_numpy(data)

    predicted_class = model_processor.predict(input_data)
    predicted_class_name = model_processor.get_class_name(predicted_class)

    return IrisPrediction(
        predicted_class=predicted_class, predicted_class_name=predicted_class_name
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
