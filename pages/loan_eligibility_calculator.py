import streamlit as st
from form_handler import FormHandler
from models.loan_eligibility.model import loan_eligibility

# Page title
st.title("Loan Eligibility Calculator")

# Defines the mappings between form fields and model fields
field_mappings = {
    "Income": "income",
    "Loan Amount": "loan_amount",
    "Credit Score": "credit_score",
    "Employment Type": "employment_type",
    "Other Loans": "other_loans",
}

# Creates the form with FormHandler, using the field mappings
loan_form = FormHandler(
    name="Loan Eligibility Form",
    button_label="Check Eligibility",
    model=loan_eligibility,
    config_path="calculator_config/loan_eligibility.json",
    field_mappings=field_mappings,
)

# Renders the form
loan_form.render()
