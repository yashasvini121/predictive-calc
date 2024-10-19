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
st.write(
	"- **Heat Load Predictor**: Estimate the heat energy requirements of your building with advanced machine learning models tailored to predict energy efficiency based on structural attributes."
)
st.write(
	"- **Cool Load Predictor**: Accurately forecast the cooling energy demands of your building using cutting-edge machine learning algorithms designed for optimizing energy efficiency."
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

st.write(
	"- **Gold Price Predictor**: Predict future gold prices leverages financial metrics and machine learning algorithm."
)

# Gold Price Predictor Section
with st.expander("Gold Price Predictor - More Information"):
	st.subheader("Introduction")
	st.write(
		"""
	The Gold Price Predictor leverages financial metrics and machine learning algorithms to forecast the price of gold (GLD). Gold prices are influenced by various economic factors, and this tool aims to provide accurate predictions based on historical data.
		"""
	)

	# Dataset section
	st.subheader("Gold Price Dataset")
	st.write(
		"""
	The dataset used for this model contains daily financial data, including stock market indices, commodity prices, and currency exchange rates. The goal is to predict the gold price (GLD) using features such as the S&P 500 Index (SPX), crude oil price (USO), silver price (SLV), and the EUR/USD exchange rate.
		"""
	)

	# Input features section
	st.subheader("Additional Variable Information")
	st.write(
		"""
	- **SPX**:  The S&P 500 index value, which tracks the performance of 500 large companies listed on stock exchanges in the United States.
	- **USO**:  The price of United States Oil Fund (USO), which reflects crude oil prices.
	- **SLV**:  The price of iShares Silver Trust (SLV), which reflects silver prices.
	- **EUR/USD**:  The Euro-to-U.S. Dollar exchange rate, which indicates the strength of the euro relative to the U.S. dollar.
	- **GLD**:  The price of SPDR Gold Shares (GLD), which is the target variable representing gold prices.
		"""
	)


#Heat Load Predictor Section
with st.expander("Heat Load Predictor - More Information"):
	st.subheader("Introduction")
	st.write(
		"""
		The Heat Load Predictor uses building characteristics and machine learning algorithms to estimate the amount of heat energy required for a building. This tool helps in optimizing energy consumption based on specific architectural and environmental features.
		"""
	)

	# Dataset section
	st.subheader("Heat Load Dataset")
	st.write(
		"""
		The dataset used for this model contains various features related to building design and environmental factors that impact energy efficiency. The goal is to predict the heat load (Y1) using features such as Relative Compactness, Surface Area, Wall Area, Roof Area, and other architectural elements.
		"""
	)

	# Input features section
	st.subheader("Additional Variable Information")
	st.write(
		"""
		- **Relative Compactness**: A measure of how compact the building's shape is, affecting its thermal properties.
		- **Surface Area**: The total external surface area of the building, impacting heat transfer.
		- **Wall Area**: The area covered by the external walls, which influences heat insulation.
		- **Roof Area**: The total area of the roof, which affects heat gain or loss.
		- **Overall Height**: The total height of the building, which influences the volume and energy needed for heating.
		- **Glazing Area**: The area of windows or glass surfaces, which can impact heat gain through sunlight.
		- **Y1 (Heat Load)**: The predicted amount of heat energy required to maintain the desired indoor temperature.
		"""
	)

#Cool Load Predictor Section
with st.expander("Cool Load Predictor - More Information"):
	st.subheader("Introduction")
	st.write(
		"""
		The Cool Load Predictor utilizes advanced machine learning models to estimate the cooling energy required for a building. By analyzing structural features and environmental factors, this tool predicts cooling loads and assists in optimizing energy efficiency.
		"""
	)

	# Dataset section
	st.subheader("Cool Load Dataset")
	st.write(
		"""
		The dataset for this model contains features related to building design and environmental factors that affect cooling efficiency. The aim is to predict the cool load (Y2) using inputs such as Relative Compactness, Surface Area, Roof Area, and other architectural parameters.
		"""
	)

	# Input features section
	st.subheader("Additional Variable Information")
	st.write(
		"""
		- **Relative Compactness**: The compactness of the building’s shape, affecting the efficiency of cooling.
		- **Surface Area**: The total external surface area, impacting how much heat is absorbed or released.
		- **Wall Area**: The external wall area, influencing heat insulation and cooling needs.
		- **Roof Area**: The area of the roof, which affects heat transfer and the cooling load.
		- **Overall Height**: The building's height, which impacts volume and energy required for cooling.
		- **Glazing Area**: The area of windows or glass surfaces, which can increase or decrease cooling efficiency based on exposure to sunlight.
		- **Y2 (Cool Load)**: The predicted amount of cooling energy required to maintain optimal indoor temperatures.
		"""
	)
