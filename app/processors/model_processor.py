import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.utils.configs import MODEL_PATH


class ModelProcessor:
    def __init__(self):
        self.model = None
        self.model_path = MODEL_PATH

    def train_and_save_model(self):
        ## Load Iris from sklearn datasets
        iris_data = load_iris()

        # Train/Test split by providing target and data details
        X_train, X_test, y_train, y_test = train_test_split(
            iris_data.data, iris_data.target, test_size=0.2, random_state=42
        )

        # Train RandomForestClassifier
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)

        # Save model weights in MODEL_PATH
        joblib.dump(model, self.model_path)

    def load_model(self):
        # Load model from MODEL_PATH if exists
        if not self.model:
            self.model = joblib.load(self.model_path)

        # Return Model weights from .pkl file
        return self.model

    def predict(self, data: np.ndarray) -> int:
        model = self.load_model()

        # Convert text to numpy array
        ## Predict class_id from pre-trained weights
        return model.predict(data)[0]

    def get_class_name(self, predicted_class: int) -> str:
        # Map class_name to the predicted class_id from predict() method
        return load_iris().target_names[predicted_class]
