import streamlit as st
import json
from models.review_sentiments.predict import predict_sentiment

# Load form configuration
with open("form_configs/review_sentiments.json") as f:
	form_config = json.load(f)

st.title("Review Sentiments")

# Generate form based on custom form config
input_data = {
	field_data["field_name"]: st.text_area(field_name, height=100)
	for field_name, field_data in form_config["Review Sentiments Form"].items()
	if field_data["type"] == "text"
}

# Submit button
if st.button("Predict"):
	review = input_data.get("review", "").strip()
	if review:
		result = predict_sentiment(review)
		st.write(f"Prediction: {result}")
	else:
		st.warning("Please enter a review before predicting.")
