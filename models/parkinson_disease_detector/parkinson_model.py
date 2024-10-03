import streamlit as st
import pickle
import numpy as np
import json

#Load the model and the scaler
filename = 'models/parkinson_disease_detector/saved_models/Model_Prediction.sav'
loaded_model = pickle.load(open(filename, 'rb'))
scaler = pickle.load(open('models/parkinson_disease_detector/saved_models/MinMaxScaler.sav', 'rb'))

# # Streamlit app

# # st.title("Parkinson's Disease Detector")

# # st.write(
# #     "This application helps to assess whether an individual is healthy or at risk of Parkinson's Disease using machine learning."
# # )

# # st.subheader("Input the following features:")

# # Load the feature specifications from JSON
# with open('form_configs/parkinson_detection.json') as json_file:
#     feature_spec = json.load(json_file)["Parkinson Detection Form"]

# # Collect inputs from the user using the specifications from the JSON
# inputs = {}
# for feature, spec in feature_spec.items():
#     inputs[feature] = st.number_input(
#         spec["field_name"], 
#         min_value=spec["min_value"], 
#         max_value=spec["max_value"]
#     )

# def get_prediction(inputs, model, scaler):
#     """Function to get the prediction based on the input data."""
#     try:
#         # Prepare the input data for prediction
#         input_data = np.array([[inputs[feature] for feature in feature_spec.keys()]])

#         # Scale the input data
#         scaled_data = scaler.transform(input_data)

#         # Make prediction
#         prediction = model.predict(scaled_data)

#         return prediction

#     except Exception as e:
#         st.error(f"An error occurred during prediction: {e}")
#         return None

# # Predict button
# if st.button('Predict'):
#     prediction = get_prediction(inputs, loaded_model, scaler)

#     # Output the result
#     if prediction is not None:
#         if prediction == 1:
#             st.error("The prediction indicates you may have Parkinson's Disease. Please consult a doctor.")
#         else:
#             st.success("The prediction indicates you are healthy.")

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


# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd

# # Load the model and the scaler
# filename = 'models/parkinson_disease_detector/saved_models/Model_Prediction.sav'
# loaded_model = pickle.load(open(filename, 'rb'))
# scaler = pickle.load(open('models/parkinson_disease_detector/saved_models/MinMaxScaler.sav', 'rb'))

# # Define the feature names as per your model training
# feature_names = [
#     "MDVP_Fo_Hz", "MDVP_Fhi_Hz", "MDVP_Flo_Hz", "MDVP_Jitter_percent", 
#     "MDVP_Jitter_Abs", "MDVP_RAP", "MDVP_PPQ", "Jitter_DDP", 
#     "MDVP_Shimmer", "MDVP_Shimmer_dB", "Shimmer_APQ3", "Shimmer_APQ5", 
#     "MDVP_APQ", "Shimmer_DDA", "NHR", "HNR", "RPDE", "DFA", 
#     "Spread1", "Spread2", "D2", "PPE"
# ]

# def disease_get_prediction(
#     MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, 
#     MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, 
#     MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, 
#     NHR, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE
# ):
#     features = [
#         float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz), 
#         float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP), 
#         float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer), 
#         float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5), 
#         float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR), 
#         float(RPDE), float(DFA), float(Spread1), float(Spread2), 
#         float(D2), float(PPE)
#     ]

#     # Convert the features to a DataFrame for consistency
#     input_data = pd.DataFrame([features], columns=feature_names)

#     # Apply the scaler to the input data
#     scaled_data = scaler.transform(input_data)

#     # Make prediction using the model
#     prediction = loaded_model.predict(scaled_data)

#     return prediction


