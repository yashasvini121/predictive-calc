# import streamlit as st

# st.set_page_config(page_title="Predictive Calc", page_icon="🧮")
	
# st.subheader("Project Description")
# st.write(
# 	"This application offers a comprehensive suite of predictive calculators to assist with various personal and health-related decisions, ranging from house price predictions and loan eligibility checks to health assessments like stress level detection and Parkinson's Disease risk evaluation."
# )

# st.subheader("Available Calculators:")
# st.write(
# 	"- **House Price Prediction**: Estimate the price of a house based on various features."
# )
# st.write(
# 	"- **Loan Eligibility**: Check your eligibility for different types of loans."
# )
# st.write(
# 	"- **Stress Level Detector**: Analyze your mental stress levels based on social media interactions."
# )
# st.write(
# 	"- **Parkinson's Disease Detector**: Quickly assess whether you may be healthy or at risk of Parkinson's Disease, powered by advanced machine learning for accurate results."
# )

import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Predictive Calc", page_icon="🧮")

# Subheader and description of the app
st.subheader("Project Description")
st.write(
    "This application offers a suite of predictive calculators for decisions like house price predictions, loan eligibility, and health assessments such as stress level and Parkinson's Disease risk evaluations."
)

# List of available calculators
st.subheader("Available Calculators:")
st.write("- **House Price Prediction**: Estimate the price of a house based on various features.")
st.write("- **Loan Eligibility**: Check your eligibility for different types of loans.")
st.write("- **Stress Level Detector**: Analyze your mental stress levels based on social media interactions.")
st.write("- **Parkinson's Disease Detector**: Assess your risk of Parkinson's Disease with advanced machine learning algorithms.")

# Parkinson's Disease Detector Section
with st.expander("Parkinson's Disease Detector - More Information"):
    st.subheader("Introduction")
    st.write("""
    Parkinson's disease (PD) is a progressive neurodegenerative disorder that primarily affects movement. It often starts with subtle symptoms such as tremors, stiffness, and slow movement.
    """)

    # Dataset section
    st.subheader("Oxford Parkinson's Disease Detection Dataset (UCI ML Repository)")
    st.write("""
    The dataset contains biomedical voice measurements from 31 people, 23 of whom have Parkinson's disease (PD). The main goal is to differentiate between healthy individuals and those with PD using the "status" column, where 0 indicates healthy and 1 indicates PD.
    """)

    # Input features section
    st.subheader("Additional Variable Information")
    st.write("""
    - **MDVP_Fo(Hz)**:  Average vocal fundamental frequency.
    - **MDVP_Fhi(Hz)**:  Maximum vocal fundamental frequency.
    - **MDVP_Flo(Hz)**:  Minimum vocal fundamental frequency.
    - **MDVP_Jitter(%)**, **MDVP_Jitter(Abs)**, **MDVP_RAP**, **MDVP_PPQ**, **Jitter_DDP**:  Measures of variation in fundamental frequency.
    - **MDVP_Shimmer**, **MDVP_Shimmer(dB)**, **Shimmer_APQ3**, **Shimmer_APQ5**, **MDVP_APQ**, **Shimmer_DDA**:  Measures of variation in amplitude.
    - **NHR**, **HNR**:  Noise-to-tonal ratio measures in the voice.
    - **status**:  Health status of the subject (1 - Parkinson's, 0 - healthy).
    - **RPDE**, **D2**:  Nonlinear dynamical complexity measures.
    - **DFA**:  Signal fractal scaling exponent.
    - **spread1**, **spread2**, **PPE**:  Nonlinear measures of fundamental frequency variation.
    """)

