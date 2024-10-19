from transformers import pipeline
import streamlit as st

@st.cache_resource(show_spinner=True)  # Cache the model loading for faster performance
def load_summarizer():
	"""Load and cache the text summarization pipeline model."""
	return pipeline("summarization", model="t5-small")

def generate_summary(text: str) -> str:
	"""Generate a summary for the given input text."""
	summarizer = load_summarizer()
	summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
	return summary[0]["summary_text"]
