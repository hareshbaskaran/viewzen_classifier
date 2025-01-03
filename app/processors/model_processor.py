import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


## todo : add "iris_model.pkl" into Configs
class ModelProcessor:
    def __init__(self):
        self.model = None
        self.model_path = "data/iris_model.pkl"

    def train_and_save_model(self):
        iris_data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris_data.data, iris_data.target, test_size=0.2, random_state=42
        )

        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        joblib.dump(model, self.model_path)

    def load_model(self):
        if not self.model:
            self.model = joblib.load(self.model_path)
        return self.model

    def predict(self, data: np.ndarray) -> int:
        model = self.load_model()
        return model.predict(data)[0]

    def get_class_name(self, predicted_class: int) -> str:
        return load_iris().target_names[predicted_class]
