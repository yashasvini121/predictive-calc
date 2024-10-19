import streamlit as st
from models.text_sumarization.predict import generate_summary

st.title("Text Summarization Tool")

st.write("Enter the text you'd like to summarize (minimum 50 words).")

user_input = st.text_area("Input Text", height=250)

# A button to initiate the summarization process
if st.button("Summarize"):
	if len(user_input.split()) < 50:
		st.warning("Please enter at least 50 words for summarization.")
	else:
		# Show a spinner while the summarization is being processed
		with st.spinner("Summarizing..."):
			summary = generate_summary(user_input)  # Call the function from predict.py
			st.subheader("Summary:")
			st.code(summary, language="text", wrap_lines=True)
