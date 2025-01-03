import joblib
import numpy as np
from sklearn.datasets import load_iris


class IrisModelHandler:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None
        self.target_names = load_iris().target_names

    def load_model(self):
        if self.model is None:
            self.model = joblib.load(self.model_path)
            print("Model loaded successfully.")

    def predict(self, input_data: np.ndarray) -> dict:
        if self.model is None:
            raise ValueError("Model is not loaded.")

        if len(input_data.shape) == 1:
            input_data = input_data.reshape(1, -1)

        predicted_class = self.model.predict(input_data)[0]
        return {
            "predicted_class": int(predicted_class),
            "predicted_class_name": self.target_names[predicted_class],
        }
