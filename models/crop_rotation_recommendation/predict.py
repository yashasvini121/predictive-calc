from models.crop_rotation_recommendation.model import crop_rotation_recommendation

# Define a function to get prediction
def get_prediction(previous_crop, soil_type, moisture_level, nitrogen, phosphorus, potassium):
    # Call the crop recommendation function with input features
    return crop_rotation_recommendation(previous_crop, soil_type, moisture_level, nitrogen, phosphorus, potassium)
