import pickle
import os
model_path = os.path.join(os.path.dirname(__file__), 'saved_models', 'model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'saved_models', 'scaler.pkl')


# Load the saved model and scaler
def load_model_and_scaler():
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    return model, scaler
