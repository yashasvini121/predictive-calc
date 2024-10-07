import streamlit as st

st.set_page_config(page_title="Predictive Calc - Machine Learning Models", page_icon="🤖")

st.title("Welcome to Predictive Calc!")
st.image('machine-learning.gif', caption='Your Hub for Predictive Insights', use_column_width=True)

st.markdown("""
## Explore Cutting-edge Machine Learning Models
**Predictive Calc** offers a powerful suite of machine learning models designed to assist you in making informed decisions. Whether it's predicting house prices, determining loan eligibility, or evaluating health risks, we have you covered.
""")

st.markdown("""
## Why Choose Predictive Calc?
- **Accurate Predictions**: Leverage state-of-the-art algorithms for highly accurate predictions.
- **User-friendly Interface**: Seamlessly interact with models tailored for real-world applications.
- **Comprehensive Calculators**: A collection of models designed for diverse decision-making needs.
- **Health & Financial Models**: Predict house prices, assess loan eligibility, and evaluate health risks such as Parkinson's and stress levels.
""")

st.markdown("""
---
**Ready to get started?** Select a calculator from the sidebar to begin your predictive journey!
""")

st.markdown("---")

# List of available calculators
st.subheader("Available Calculators:")
st.write(
	"- **Bitcoin Price Predictor**: The Bitcoin Price Predictor form allows users to input the current price, moving average, and market sentiment to forecast potential price movements."
)
st.write(
	"- **Customer Income Estimation**: Estimate the annual income of a person based on socio-economic and demographic information."
)
st.write(
	"- **House Price Prediction**: Estimate the price of a house based on various features."
)
st.write("- **Loan Eligibility**: Check your eligibility for different types of loans.")
st.write(
	"- **Stress Level Detector**: Analyze your mental stress levels based on social media interactions."
)
st.write(
	"- **Parkinson's Disease Detector**: Assess your risk of Parkinson's Disease with advanced machine learning algorithms."
)

# Parkinson's Disease Detector Section
with st.expander("Parkinson's Disease Detector - More Information"):
	st.subheader("Introduction")
	st.write(
		"""
	Parkinson's disease (PD) is a progressive neurodegenerative disorder that primarily affects movement. It often starts with subtle symptoms such as tremors, stiffness, and slow movement.
	"""
	)

	# Dataset section
	st.subheader("Oxford Parkinson's Disease Detection Dataset (UCI ML Repository)")
	st.write(
		"""
	The dataset contains biomedical voice measurements from 31 people, 23 of whom have Parkinson's disease (PD). The main goal is to differentiate between healthy individuals and those with PD using the "status" column, where 0 indicates healthy and 1 indicates PD.
	"""
	)

	# Input features section
	st.subheader("Additional Variable Information")
	st.write(
		"""
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
	"""
	)
