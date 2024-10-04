import streamlit as st

# Configure page
st.set_page_config(page_title="Predictive Calc", page_icon="🧮", layout="centered", initial_sidebar_state="expanded")

st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSubheader {
        color: #2C3E50;
        font-weight: bold;
        margin-top: 20px;
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("Predictive Calc 🧮")
st.write("Welcome to the **Predictive Calc** app! Your go-to tool for making smarter financial decisions.")

col1, col2 = st.columns(2)

with col1:
	# Project description
	st.subheader("Project Description")
	st.write(
		"""
		This application offers a set of calculators to assist with various financial decisions, including:
		- House Price Predictions
		- Loan Eligibility Assessments
		- Stress Level Detection based on social media interactions
		"""
	)

with col2:
	# Available Calculators Section with icons
	st.subheader("Available Calculators:")

	st.write("🏡 **House Price Prediction**")
	st.write("Estimate the price of a house based on various features like location, size, and amenities.")

	st.write("💰 **Loan Eligibility**")
	st.write("Check your eligibility for different types of loans based on your financial profile.")

	st.write("🧠 **Stress Level Detector**")
	st.write("Analyze your mental stress levels based on your social media interactions.")
