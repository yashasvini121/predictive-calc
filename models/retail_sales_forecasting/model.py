import pickle
import os
import pandas as pd
import numpy as np

# Paths to model and scaler
model_path = os.path.join("models", "model.pkl")
scaler_path = os.path.join("models", "scaler.pkl")

# Load the model and scaler
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

def predict(input_data):
    """
    Accepts input_data as a dictionary and returns the prediction.
    Expected keys: 'store_number', 'department_number', 'date', 'is_holiday'
    """
    # Convert date to timestamp and structure data for the model
    input_data['date'] = pd.to_datetime(input_data['date']).timestamp()
    input_df = pd.DataFrame([input_data])

    # Scale the input data
    input_df_scaled = scaler.transform(input_df)

    # Make the prediction
    prediction = model.predict(input_df_scaled)
    return prediction[0]
