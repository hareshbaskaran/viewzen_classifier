import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from iris_classifier.utils.configs import DATASET_PATH, DATASINK_PATH
import joblib

df = pd.read_csv(DATASET_PATH)

## get the dataframe from conectors

y = df['Species']
x = df.drop(['Species', 'Id'], axis = 1)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=60)

model = DecisionTreeClassifier(random_state=60)
model.fit(x_train,y_train)


# Save the model
joblib.dump(model, DATASINK_PATH)


