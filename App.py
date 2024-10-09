import streamlit as st

st.set_page_config(page_title="Predictive Calc", page_icon="🧮")
	
st.subheader("Project Description")
st.write(
	"This application provides a set of calculators to help you with financial decisions, including house price predictions and loan eligibility assessments."
)

st.subheader("Available Calculators:")
st.write(
	"- **House Price Prediction**: Estimate the price of a house based on various features."
)
st.write(
	"- **Loan Eligibility**: The Loan Prediction Calculator is designed to assess an individual's eligibility for a loan by considering a range of key financial inputs. By collecting essential information such as the number of dependents, education level, employment status, annual income, loan amount, loan term, CIBIL score, and various asset values, this calculator aims to provide a comprehensive evaluation of the applicant's financial situation. By analyzing these inputs, the calculator can offer more accurate predictions regarding loan approval, helping users make informed decisions about their borrowing potential."
)
