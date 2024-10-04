import streamlit as st
from styling import load_css, render_layout  # Import both load_css and render_layout functions

# Set page configuration (this must be the first Streamlit command)
st.set_page_config(page_title="Predictive Calc", page_icon="🧮")

# Reducing whitespace on the top of the page
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# Load custom CSS
load_css("changes/style.css")  # Make sure this path is correct

# Render the two-column layout with project description and calculators
render_layout()
