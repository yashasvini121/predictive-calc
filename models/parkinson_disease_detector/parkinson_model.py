import streamlit as st
import pickle
import numpy as np
import json

#Load the model and the scaler
filename = 'models/parkinson_disease_detector/saved_models/Model_Prediction.sav'
loaded_model = pickle.load(open(filename, 'rb'))
scaler = pickle.load(open('models/parkinson_disease_detector/saved_models/MinMaxScaler.sav', 'rb'))

def disease_get_prediction(MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz,
                           MDVP_Jitter_percent, MDVP_Jitter_Abs,
                           MDVP_RAP, MDVP_PPQ, Jitter_DDP,
                           MDVP_Shimmer, MDVP_Shimmer_dB,
                           Shimmer_APQ3, Shimmer_APQ5,
                           MDVP_APQ, Shimmer_DDA, NHR,
                           HNR, RPDE, DFA, spread1,
                           spread2, D2, PPE):
    features = [
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
    ]

    # Convert the features to a numpy array and reshape it for scaling
    input_data = np.array([features]).reshape(1, -1)

    # Apply the scaler to the input data
    scaled_data = scaler.transform(input_data)

    # Make prediction using the model
    prediction = loaded_model.predict(scaled_data)

    return prediction
