import streamlit as st
import json
from models.cervical_cancer.predict import predict

# Load form configuration
with open('form_configs/cervical_cancer.json') as f:
    form_config = json.load(f)

st.title(form_config['title'])

# Generate form dynamically
inputs = {}
for field in form_config['inputs']:
    if field['type'] == 'number':
        inputs[field['key']] = st.number_input(field['label'])
    elif field['type'] == 'select':
        inputs[field['key']] = st.selectbox(field['label'], field['options'])

# Predict button
if st.button('Predict Cervical Cancer Risk'):
    input_data = [inputs[key] for key in inputs.keys()]
    result = predict(input_data)
    st.write(f"Prediction: {'Positive' if result == 1 else 'Negative'}")
