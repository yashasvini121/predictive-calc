import streamlit as st

# Load custom CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
# Function to render the two-column layout with project description and calculators
def render_layout():
    st.title("Predictive Calc 🧮")
    st.write("Welcome to the **Predictive Calc** app! Your go-to tool for making smarter financial decisions.")
    
    # Two-column layout
    col1, col2 = st.columns(2)

    with col1:
        # Project description section
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
