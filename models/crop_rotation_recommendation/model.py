import joblib
import pandas as pd

# Load the trained crop recommendation model
crop_model = joblib.load('models/crop_rotation_recommendation/saved_models/crop_rotation_recommendation_model.pkl')

# Define the function to make predictions
def crop_rotation_recommendation(previous_crop, soil_type, moisture_level, nitrogen, phosphorus, potassium):
    # Define the mappings (previous crop and soil type mappings)
    previous_crop_mapping = {
        'Groundnut': 1,
        'Millets': 2,
        'Wheat': 3,
        'Maize': 4,
        'Cotton': 5,
        'Sorghum': 6,
        'Barley': 7
    }

    soil_type_mapping = {
        'Loamy': 1,
        'Clayey': 2,
        'Sandy': 3,
        'Saline': 4,
    }

    crop_mapping = {
        1: 'Wheat',
        2: 'Rice',
        3: 'Millets',
        4: 'Cotton',
        5: 'Groundnut',
        6: 'Maize',
        7: 'Sorghum',
        8: 'Barley',
    }

    # Prepare input data for the model
    input_data = pd.DataFrame([{
        "Previous Crop": previous_crop_mapping.get(previous_crop, -1),
        "Soil Type": soil_type_mapping.get(soil_type, -1),
        "Moisture Level": moisture_level,
        "Nitrogen (N)": nitrogen,
        "Phosphorus (P)": phosphorus,
        "Potassium (K)": potassium
    }])

    # Make a prediction using the model
    prediction = crop_model.predict(input_data)
    
    return crop_mapping.get(prediction[0])  # Return the predicted crop class
