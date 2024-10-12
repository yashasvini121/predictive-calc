from joblib import load

# Load the trained model for gold price prediction
model = load('models/gold_price_prediction/saved_models/random_forest_model.joblib')

def gold_price_prediction(spx, uso, slv, eur_usd):
    # Feature extraction
    features = [
        float(spx),
        float(uso),
        float(slv),
        float(eur_usd)
    ]

    # Predict the gold price (GLD)
    prediction = model.predict([features])[0]
    
    return prediction
