import pickle
import numpy as np


def load_model():
    with open('models/customer_income/saved_models/CImodel.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('models/customer_income/saved_models/CIscaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler


def predict(features):
    model, scaler = load_model()
    features_array = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(features_array)
    prediction = model.predict(scaled_features)
    return prediction


