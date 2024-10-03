# import streamlit as st
# import pickle
# import numpy as np
# from streamlit_option_menu import option_menu

# # Load the model and the scaler
# filename = 'Model_Prediction.sav'
# loaded_model = pickle.load(open(filename, 'rb'))
# scaler = pickle.load(open('MinMaxScaler.sav', 'rb'))

# # Set up navigation menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Navigation",  # Required
#         options=["Variable Information", "Parkinson's Detector"],  # Required
#         icons=["info", "activity"],  # Optional
#         menu_icon="cast",  # Optional
#         default_index=0,  # Optional
#     )

# # Page 1: Variable Information
# if selected == "Variable Information":
#     st.title("Parkinson's Disease Detection - Variable Information")
    
#     st.write("""
#     Here is a detailed description of the variables used for predicting Parkinson's Disease:
#     """)
    
#     st.subheader("1. Name")
#     st.write("**Description**: ASCII subject name and recording number.")

#     st.subheader("2. MDVP:Fo(Hz)")
#     st.write("**Description**: Average vocal fundamental frequency (in Hz).")

#     st.subheader("3. MDVP:Fhi(Hz)")
#     st.write("**Description**: Maximum vocal fundamental frequency (in Hz).")

#     st.subheader("4. MDVP:Flo(Hz)")
#     st.write("**Description**: Minimum vocal fundamental frequency (in Hz).")

#     st.subheader("5. MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP")
#     st.write("**Description**: Various measures of variation in fundamental frequency.")

#     st.subheader("6. MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5, MDVP:APQ, Shimmer:DDA")
#     st.write("**Description**: Various measures of variation in amplitude.")

#     st.subheader("7. NHR, HNR")
#     st.write("**Description**: Two measures of the ratio of noise to tonal components in the voice.")

#     st.subheader("8. Status")
#     st.write("**Description**: Health status of the subject (1 = Parkinson's, 0 = healthy).")

#     st.subheader("9. RPDE, D2")
#     st.write("**Description**: Two nonlinear dynamical complexity measures.")

#     st.subheader("10. DFA")
#     st.write("**Description**: Signal fractal scaling exponent.")

#     st.subheader("11. Spread1, Spread2, PPE")
#     st.write("**Description**: Three nonlinear measures of fundamental frequency variation.")

# # Page 2: Parkinson's Detector
# if selected == "Parkinson's Detector":
#     st.title("Parkinson's Disease Detector")

#     st.write(
#         "This application helps to assess whether an individual is healthy or at risk of Parkinson's Disease using machine learning."
#     )

#     st.subheader("Input the following features:")
#     # Collect inputs from the user with specified ranges
#     mdvp_fo = st.number_input("MDVP:Fo(Hz)", min_value=88.0, max_value=260.0, format="%.6f")
#     mdvp_fhi = st.number_input("MDVP:Fhi(Hz)", min_value=102.0, max_value=592.0, format="%.6f")
#     mdvp_flo = st.number_input("MDVP:Flo(Hz)", min_value=65.0, max_value=240.0, format="%.6f")
#     mdvp_jitper = st.number_input("MDVP:Jitter(%)", min_value=0.001, max_value=0.033, format="%.6f")
#     mdvp_jitabs = st.number_input("MDVP:Jitter(Abs)", min_value=0.00002, max_value=0.0002, format="%.6f")
#     mdvp_rap = st.number_input("MDVP:RAP", min_value=0.0006, max_value=0.02, format="%.6f")
#     mdvp_ppq = st.number_input("MDVP:PPQ", min_value=0.0009, max_value=0.02, format="%.6f")
#     jitter_ddp = st.number_input("Jitter:DDP", min_value=0.002, max_value=0.065, format="%.6f")
#     mdvp_shim = st.number_input("MDVP:Shimmer", min_value=0.009, max_value=0.12, format="%.6f")
#     mdvp_shim_db = st.number_input("MDVP:Shimmer(dB)", min_value=0.085, max_value=1.302, format="%.6f")
#     shimm_apq3 = st.number_input("Shimmer:APQ3", min_value=0.004, max_value=0.056, format="%.6f")
#     shimm_apq5 = st.number_input("Shimmer:APQ5", min_value=0.005, max_value=0.08, format="%.6f")
#     mdvp_apq = st.number_input("MDVP:APQ", min_value=0.007, max_value=0.14, format="%.6f")
#     shimm_dda = st.number_input("Shimmer:DDA", min_value=0.013, max_value=0.17, format="%.6f")
#     nhr = st.number_input("NHR", min_value=0.0006, max_value=0.31, format="%.6f")
#     hnr = st.number_input("HNR", min_value=8.0, max_value=33.0, format="%.6f")
#     rpde = st.number_input("RPDE", min_value=0.25, max_value=0.68, format="%.6f")
#     dfa = st.number_input("DFA", min_value=0.57, max_value=0.82, format="%.6f")
#     spread1 = st.number_input("Spread1", min_value=-7.0, max_value=-2.0, format="%.6f")
#     spread2 = st.number_input("Spread2", min_value=0.006, max_value=0.45, format="%.6f")
#     d2 = st.number_input("D2", min_value=1.42, max_value=3.67, format="%.6f")
#     ppe = st.number_input("PPE", min_value=0.04, max_value=0.5, format="%.6f")

#     # Predict button
#     if st.button('Predict'):
#         try:
#             # Prepare the input data for prediction
#             input_data = np.array([[mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitper, mdvp_jitabs, mdvp_rap, mdvp_ppq,
#                                     jitter_ddp, mdvp_shim, mdvp_shim_db, shimm_apq3, shimm_apq5, mdvp_apq,
#                                     shimm_dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])

#             # Scale the input data
#             scaled_data = scaler.transform(input_data)

#             # Make prediction
#             prediction = loaded_model.predict(scaled_data)

#             # Output the result
#             if prediction == 1:
#                 st.error("The prediction indicates you may have Parkinson's Disease. Please consult a doctor.")
#             else:
#                 st.success("The prediction indicates you are healthy.")

#         except Exception as e:
#             st.error(f"An error occurred: {e}")
