import streamlit as st
import importlib.util
import json
from form_handler import FormHandler


# Utility to dynamically import modules
def load_module_from_path(module_name, file_path):
	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


class PageHandler:
	def __init__(self, config_file_path):
		# Load the page configuration from JSON
		with open(config_file_path, "r") as f:
			self.pages = json.load(f)

	def render_page(self, page_name: str):
		# Check if the requested page exists in the JSON config
		if page_name not in self.pages:
			st.error("Page not found!")
			return

		page = self.pages[page_name]
		page_title = page.get("page_title", "Untitled Page")
		page_icon = page.get("page_icon", "📄")  # Default to a generic icon
		model_predict_file_path = page.get("model_predict_file_path")
		form_config_path = page.get("form_config_path")
		tabs = page.get("tabs", [])

		# Set Streamlit's page config with the title and icon
		st.set_page_config(page_title=page_title, page_icon=page_icon)

		# Dynamically load the model prediction file
		model_module = load_module_from_path(
			f"{page_name}_model", model_predict_file_path
		)
		model_function = getattr(
			model_module, "get_prediction", None
		)  # or relevant model function

		# Create the tabs for the page
		tab_objects = st.tabs([tab["name"] for tab in tabs])

		# Iterate through the tabs to render them
		for i, tab in enumerate(tabs):
			with tab_objects[i]:
				if tab["type"] == "form":
					self.render_form(tab["form_name"], model_function, form_config_path)
				elif tab["type"] == "model_details":
					self.render_model_details(model_module)

	def render_form(self, form_name: str, model_function, form_config_path: str):
		form_handler = FormHandler(
			name=form_name,
			button_label="Predict",
			model=model_function,
			config_path=form_config_path,
		)

		# Render the form on the Streamlit page
		form_handler.render()

	def render_model_details(self, model_module):
		# Dynamically load and call the model details function
		model_details_function = getattr(model_module, "model_details", None)

		if model_details_function:
			metrics, prediction_plot, error_plot, performance_plot = model_details_function().evaluate()

			st.header("Model Details")
			st.subheader(f"Model Accuracy: {metrics['Test_R2']:.2%}")

			#mentioning the title of the scores 
			st.subheader(f"Scores: Training: {metrics['Train_R2']:.2f}, Testing: {metrics['Test_R2']:.2f}")

			# Display the scatter plot for predicted vs actual values
			#used clear_figure to clear the plot once displayed to avoid conflict 
			st.subheader("Model Prediction Plot")
			st.pyplot(prediction_plot, clear_figure=True)

			st.subheader("Error Plot")
			st.pyplot(error_plot, clear_figure=True)
			
			st.subheader("Model Performance Plot")
			st.pyplot(performance_plot, clear_figure=True)
