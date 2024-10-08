import pickle
import numpy as np

def load_model():
    with open('models/cervical_cancer/saved_models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('models/cervical_cancer/saved_models/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    return model, scaler

def predict(input_data):
    model, scaler = load_model()
    input_scaled = scaler.transform(np.array(input_data).reshape(1, -1))
    prediction = model.predict(input_scaled)
    return prediction[0]
