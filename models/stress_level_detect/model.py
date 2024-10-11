# model.py
from joblib import load
import numpy as np

# Load the trained Random Forest model
model = load('models/stress_level_detect/saved_models/random_forest_model.joblib')

def validate_input(value, min_val=None, max_val=None):
    """Validates and converts input to the correct type, ensuring values are within specified ranges."""
    try:
        value = float(value)
        if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
            raise ValueError(f"Value {value} out of allowed range: [{min_val}, {max_val}]")
    except ValueError as e:
        return str(e)  # Return error message
    return value

def stress_level_prediction(age, freq_no_purpose, freq_distracted, restless, worry_level, difficulty_concentrating,
                            compare_to_successful_people, feelings_about_comparisons, freq_seeking_validation,
                            freq_feeling_depressed, interest_fluctuation, sleep_issues):
    """
    Predicts the stress level using a trained Random Forest model and the provided features.
    """

    # Input validation and feature extraction
    features = [
        validate_input(age, 0, 100),
        validate_input(freq_no_purpose, 0, 10),
        validate_input(freq_distracted, 0, 10),
        validate_input(restless, 0, 10),
        validate_input(worry_level, 0, 10),
        validate_input(difficulty_concentrating, 0, 10),
        validate_input(compare_to_successful_people, 0, 10),
        validate_input(feelings_about_comparisons, 0, 10),
        validate_input(freq_seeking_validation, 0, 10),
        validate_input(freq_feeling_depressed, 0, 10),
        validate_input(interest_fluctuation, 0, 10),
        validate_input(sleep_issues, 0, 10)
    ]
    
    # Ensure no errors in feature validation
    if any(isinstance(f, str) for f in features):
        return "Invalid input values. Please provide valid numerical data in the correct range."
    
    features = np.array(features).reshape(1, -1)

    # Prediction using the model (use `predict_proba` for probability-based prediction)
    prediction_proba = model.predict_proba(features)[0]  # Returns probabilities for each class
    predicted_class = np.argmax(prediction_proba)  # Get the class with highest probability

    return predicted_class, prediction_proba[predicted_class]
