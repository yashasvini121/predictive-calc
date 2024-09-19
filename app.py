import streamlit as st
import pages.house_price_calculator
import pages.loan_eligibility_calculator


def main():
    st.sidebar.title("Calculator App")

    # Page selection
    page = st.sidebar.selectbox(
        "Select a Calculator", ["Home", "House Price Prediction", "Loan Eligibility"]
    )

    # Home page
    if page == "Home":
        st.title("Welcome to the Calculator App")
        st.write("Select a calculator from the sidebar to get started.")

    # Show the page content based on selection
    elif page == "House Price Prediction":
        # No need to call a function, just import and let the page render
        pages.house_price_calculator

    elif page == "Loan Eligibility":
        pages.loan_eligibility_calculator


if __name__ == "__main__":
    main()
