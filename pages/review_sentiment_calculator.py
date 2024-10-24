import streamlit as st
import json
from models.Review_sentiments.predict import predict_sentiment

# Load form configuration
with open("form_configs/review_sentiments.json", "r") as f:
    form_config = json.load(f)

st.title(form_config['title'])

# Generate form based on config
input_data = {}
for field in form_config['fields']:
    if field['type'] == 'text':
        input_data[field['name']] = st.text_area(field['label'], height=100)

# Submit button
if st.button("Predict"):
    result = predict_sentiment(input_data['text'])
    st.write(f"Prediction: {result}")
