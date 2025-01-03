from app.models.iris import IrisInput
import numpy as np
# Helper function to convert the model data to numpy array
def convert_model_to_numpy(model_instance: IrisInput) -> np.ndarray:
    model_dict = model_instance.dict()
    return np.array([list(model_dict.values())])