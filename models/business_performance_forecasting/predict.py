# import os
import numpy as np
from models.business_performance_forecasting.model import load_model_and_scaler  # Import the function from model.py

# Define the prediction function
def get_prediction(RnD_Spend, Administration, Marketing_Spend, State):
    # Load the model and scaler
    model, scaler = load_model_and_scaler()
    # Prepare input features as a NumPy array
    input_data = np.array([[RnD_Spend, Administration, Marketing_Spend, State]])
    
    # Apply the scaler
    scaled_data = scaler.transform(input_data)
    scaled_data = scaled_data.astype(float)  
    
    # Make prediction using the loaded model
    prediction = model.predict(scaled_data)
    
    return prediction[0]  # Return the predicted profit

