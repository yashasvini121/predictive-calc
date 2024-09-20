import streamlit as st
from form_handler import FormHandler
from models.loan_eligibility.model import loan_eligibility

# Page title
st.set_page_config(page_title="Loan Eligibility", page_icon="💰")
st.title("Loan Eligibility Calculator")

# Creates the form with FormHandler, using the field mappings
loan_form = FormHandler(
    name="Loan Eligibility Form",
    button_label="Check Eligibility",
    model=loan_eligibility,
    config_path="form_configs/loan_eligibility.json",
)

# Renders the form
loan_form.render()
