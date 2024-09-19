import streamlit as st
from form_handler import FormHandler
from models.house_price.model import house_price_prediction_model

# Page Title
st.title("House Price Prediction Calculator")

# Defines the field mappings for the form
field_mappings = {
    "Area (in square feet)": "area",
    "Near Main Road": "mainroad",
    "Guest Room": "guestroom",
    "Basement": "basement",
    "Hot Water Heating": "hotwaterheating",
    "Air Conditioning": "airconditioning",
    "Preferred Area": "prefarea",
    "Number of Bedrooms": "bedrooms",
    "Number of Bathrooms": "bathrooms",
    "Number of Stories": "stories",
    "Parking Spaces": "parking",
    "Furnishing Status": "furnishingstatus",
}

# Creates the form with FormHandler, using the field mappings
house_form = FormHandler(
    name="House Price Estimator",
    button_label="Predict Price",
    model=house_price_prediction_model,
    config_path="calculator_config/house_price.json",
    field_mappings=field_mappings,
)

# Render the form
house_form.render()
