from fastapi import FastAPI
from iris_classifier.utils.models import UserInput
app = FastAPI()


@app.get("/helloworld")
def root():
    return " hello world"
@app.post("/predict")
async def predict(data: UserInput):
    pass

