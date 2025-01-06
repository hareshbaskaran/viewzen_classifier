import streamlit as st
import requests
from utils.configs import API_ENDPOINT_URL

st.title("Iris Flower Prediction")
st.write("Please provide the following DEtails about iris :")

sepal_length = st.number_input(
    "Sepal Length (cm)", min_value=0.0, max_value=10.0, step=0.1
)
sepal_width = st.number_input(
    "Sepal Width (cm)", min_value=0.0, max_value=10.0, step=0.1
)
petal_length = st.number_input(
    "Petal Length (cm)", min_value=0.0, max_value=10.0, step=0.1
)
petal_width = st.number_input(
    "Petal Width (cm)", min_value=0.0, max_value=10.0, step=0.1
)

if st.button("Predict"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    # Send JSON data in the request
    response = requests.post(API_ENDPOINT_URL, json=data)

    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Predicted Class: {prediction['predicted_class']}")
        st.write(f"Predicted Class Name: {prediction['predicted_class_name']}")
    else:
        st.write(f"Error in prediction. Status code: {response.status_code}")
