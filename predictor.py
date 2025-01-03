import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import numpy as np
from utils.schemas import PredictionData


class IrisModelHandler:
    def __init__(self, model_path: str, target_names: list[str]):
        self.model_path = model_path
        self.model = None
        self.target_names = target_names

    def train_and_save_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        # Evaluate the model
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, target_names=self.target_names)
        print(f"Model Accuracy: {accuracy}\nClassification Report:\n{report}")

        # Save the trained model
        joblib.dump(clf, self.model_path)
        print(f"Model saved to {self.model_path}")

    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at {self.model_path}")
        self.model = joblib.load(self.model_path)
        print("Model loaded successfully.")

    def predict(self, input_data: np.ndarray) -> PredictionData:
        if self.model is None:
            raise ValueError("Model is not loaded.")

        # Ensure input data is 2D
        if len(input_data.shape) == 1:
            input_data = input_data.reshape(1, -1)

        predicted_class = self.model.predict(input_data)[0]
        return PredictionData(
            predicted_label=predicted_class,
            predicted_name=self.target_names[predicted_class]
        )
