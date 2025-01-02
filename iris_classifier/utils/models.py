from pydantic import BaseModel

## SepalLengthCm
## SepalWidthCm
## PetalLengthCm
## PetalWidthCm

## Species

class UserInput(BaseModel):
    SepalLength : float
    SepalWidth : float
    PetalLength : float
    PetalWidth : float


