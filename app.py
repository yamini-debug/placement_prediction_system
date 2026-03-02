import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# App title
st.title("Placement Prediction System")

st.write("Enter the details below to check placement status.")

# Input fields (example: IQ and CGPA)
iq = st.number_input("Enter IQ", min_value=0)
cgpa = st.number_input("Enter CGPA", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict"):

    # Prepare input
    features = np.array([[iq, cgpa]])

    # Prediction
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Prediction: Placed ✅")
    else:
        st.error("Prediction: Not Placed ❌")
