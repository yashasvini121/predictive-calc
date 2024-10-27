import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# Load the model and the scaler
model_path = 'models/parkinson_disease_detection_svm/saved_models/Model_Prediction.sav'
scaler_path = 'models/parkinson_disease_detection_svm/saved_models/MinMaxScaler.sav'

# Load the pre-trained model and scaler using pickle
loaded_model = pickle.load(open(model_path, 'rb'))
scaler = pickle.load(open(scaler_path, 'rb'))

# Define the prediction function
def disease_get_prediction(MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz,
                           MDVP_Jitter_percent, MDVP_Jitter_Abs,
                           MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                           MDVP_Shimmer, MDVP_Shimmer_dB,
                           Shimmer_APQ3, Shimmer_APQ5,
                           MDVP_APQ, Shimmer_DDA, NHR,
                           HNR, RPDE, DFA, spread1,
                           spread2, D2, PPE):
    features = np.array([[
        float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),
        float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs),
        float(MDVP_RAP), float(MDVP_PPQ), float(Jitter_DDP),
        float(MDVP_Shimmer), float(MDVP_Shimmer_dB),
        float(Shimmer_APQ3), float(Shimmer_APQ5),
        float(MDVP_APQ), float(Shimmer_DDA),
        float(NHR), float(HNR),
        float(RPDE), float(DFA),
        float(spread1), float(spread2),
        float(D2), float(PPE)
    ]])

    # Apply the scaler
    scaled_data = scaler.transform(features)

    # Make prediction
    prediction = loaded_model.predict(scaled_data)

    return prediction