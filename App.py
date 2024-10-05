import streamlit as st
from styling import load_css, render_layout  # Import both load_css and render_layout functions

<<<<<<< HEAD
# Set page configuration (this must be the first Streamlit command)
st.set_page_config(page_title="Predictive Calc", page_icon="🧮")

# Reducing whitespace on the top of the page
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# Load custom CSS
load_css("changes/style.css")  # Make sure this path is correct

# Render the two-column layout with project description and calculators
render_layout()
=======
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
>>>>>>> 56b5e0270550d5c728bc69e577c2b555f17b0210
