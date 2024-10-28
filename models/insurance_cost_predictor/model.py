from joblib import load

# Load the trained model for insurance cost prediction
model = load("models/insurance_cost_predictor/saved_models/insurance_model.pkl")

def insurance_cost_prediction(age, sex, bmi, children, smoker, region):
    # Feature extraction and conversions
    sex_value = 0 if sex.lower() == 'male' else 1  # 0 for male, 1 for female
    smoker_value = 0 if smoker.lower() == 'yes' else 1  # 0 for smoker, 1 for non-smoker
    region_dict = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}
    region_value = region_dict.get(region.lower(), -1)  # Convert region to numerical value

    # Prepare features for prediction
    features = [
        float(age),
        float(sex_value),
        float(bmi),
        int(children),
        float(smoker_value),
        float(region_value)
    ]

    # Predict the insurance cost (charges)
    prediction = model.predict([features])[0]
    
    return prediction
