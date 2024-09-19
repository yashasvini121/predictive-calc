import streamlit as st
from form_handler import FormHandler
from models.loan_eligibility.model import loan_eligibility

# Define the mappings between form fields and model fields
field_mappings = {
    "Income": "income",
    "Loan Amount": "loan_amount",
    "Credit Score": "credit_score",
    "Employment Type": "employment_type",
    "Other Loans": "other_loans",
}

# Set the title for the page
st.title("Loan Eligibility Calculator")

# Create the form with FormHandler, using the field mappings
loan_form = FormHandler(
    name="Loan Eligibility Form",
    button_label="Check Eligibility",
    model=loan_eligibility,
    config_path="calculator_config/loan_eligibility.json",
    field_mappings=field_mappings,
)

# Render the form
loan_form.render()
