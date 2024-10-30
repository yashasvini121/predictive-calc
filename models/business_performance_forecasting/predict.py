import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
from models.business_performance_forecasting.model import load_model_and_scaler  # Import the function from model.py

# Define the prediction function
def get_prediction(RnD_Spend, Administration, Marketing_Spend, State):
    # Load the model and scalers
    model, scaler = load_model_and_scaler()
    # Prepare input features as a NumPy array
    input_data = np.array([[RnD_Spend, Administration, Marketing_Spend, State]])
    
    # Apply the scaler
    scaled_data = scaler.transform(input_data)
    scaled_data = scaled_data.astype(float)  
    
    # Make prediction using the loaded model
    prediction = model.predict(scaled_data)
    
    return prediction[0]  # Return the predicted profit


class ModelEvaluation:
    def __init__(self):
        metrics_file= os.path.join(os.path.dirname(__file__), 'saved_models', 'evaluation_results.pkl')
        # Load evaluation metrics from a pickle file
        with open(metrics_file, "rb") as f:
            self.metrics = pickle.load(f)
        print("Loaded metrics:", self.metrics)
    def evaluate(self):
        metrics = self.metrics       
        return metrics, None, None, None

def model_details():
    evaluator = ModelEvaluation()
    return evaluator

