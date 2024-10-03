import streamlit as st

st.set_page_config(page_title="Predictive Calc", page_icon="🧮")
	
st.subheader("Project Description")
st.write(
	"This application offers a comprehensive suite of predictive calculators to assist with various personal and health-related decisions, ranging from house price predictions and loan eligibility checks to health assessments like stress level detection and Parkinson's Disease risk evaluation."
)

st.subheader("Available Calculators:")
st.write(
	"- **House Price Prediction**: Estimate the price of a house based on various features."
)
st.write(
	"- **Loan Eligibility**: Check your eligibility for different types of loans."
)
st.write(
	"- **Stress Level Detector**: Analyze your mental stress levels based on social media interactions."
)
st.write(
	"- **Parkinson's Disease Detector**: Quickly assess whether you may be healthy or at risk of Parkinson's Disease, powered by advanced machine learning for accurate results."
)
