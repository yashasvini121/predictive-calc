import streamlit as st

def home():
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
    - **Health & Financial Models**: Predict house prices,Customer churn probability, assess loan eligibility, and evaluate health risks such as Parkinson's and stress levels.
    """)

    st.markdown("""
    ---
    **Ready to get started?** Select a calculator from the sidebar to begin your predictive journey!
    """)

home()
