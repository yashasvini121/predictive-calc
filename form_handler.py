import streamlit as st
import json
from typing import Dict, Any


class FormHandler:
	"""
	A class to handle rendering a form in Streamlit based on a configuration file.

	Attributes:
		name (str): The name of the form to be rendered.
		button_label (str): The label for the submit button.
		model (callable): The model function to be called with form data.
		config_path (str): Path to the configuration JSON file.
		
		Structure of the configuration JSON file:
		{
			"Form Name": {
				"field_label": {
					"field_name": "field_name",
					"type": "field_type",
					"default_value": "default_value",
					"min_value": min_value,
					"max_value": max_value,
					"step": step,
					"options": ["option1", "option2"],
				},
				...
			}
		}
	"""

	def __init__(
		self, name: str, button_label: str, model: callable, config_path: str
	) -> None:
		"""
		Initializes the FormHandler with the provided parameters.

		Parameters:
			name (str): The name of the form to be rendered.
			button_label (str): The label for the submit button.
			model (callable): The model function to be called with form data.
			config_path (str): Path to the configuration JSON file.
		"""
		self.name = name
		self.button_label = button_label
		self.model = model
		self.config_path = config_path
		self.fields = self.load_fields_from_config()

	def load_fields_from_config(self) -> Dict[str, Dict[str, Any]]:
		"""
		Loads form fields from the configuration JSON file.

		Returns:
			Dict[str, Dict[str, Any]]: A dictionary of form fields and their attributes.
		"""
		
		# Try-except block to handle the exception if file not found or if parsing has parsing issues in JSON
		try:
			with open(self.config_path, "r") as f:
				config = json.load(f)
			return config.get(self.name, {})
		except FileNotFoundError:
			st.error(f"Configuration file not found: {self.config_path}")
			return {}
		except json.JSONDecodeError:
			st.error(f"Error parsing the configuration file: {self.config_path}")
			return {}


	def render(self) -> None:
		"""
		Renders the form in the Streamlit application.

		This method collects user input and, upon form submission, calls the specified model
		with the collected data mapped to the appropriate field names from the config file.
		"""
		# Dictionary to hold form data
		form_data: Dict[str, Any] = {}

		# Loop over the fields in the form
		for label, attributes in self.fields.items():
			field_type = attributes.get("type")
			field_name = attributes.get(
				"field_name", label
			)  # Use field_name from the config

			#Handle different types of input fields
			if field_type == "number":
				form_data[field_name] = st.number_input(
					label,
					value=attributes.get("default_value"),
					min_value=attributes.get("min_value"),
					max_value=attributes.get("max_value"),
					step=attributes.get("step", 1),
				)
				
			elif field_type == "float":  # New case for float values
				form_data[field_name] = st.number_input(
					label,
					value=attributes.get("default_value"),  
					min_value=attributes.get("min_value"),
					max_value=attributes.get("max_value"),
					step=attributes.get("step"),
					format="%.6f"  # format to 6 decimal places
				)

			elif field_type == "dropdown":
				form_data[field_name] = st.selectbox(
					label,
					options=attributes.get("options"),
					index=attributes.get("options").index(
						attributes.get("default_value")
					),
				)
			elif field_type == "range":
				form_data[field_name] = st.slider(
					label,
					min_value=attributes.get("min_value"),
					max_value=attributes.get("max_value"),
					value=tuple(attributes.get("default_value")),  # type: ignore
				)
			elif field_type == "multiselect":
				form_data[field_name] = st.multiselect(
					label,
					options=attributes.get("options"),
					default=attributes.get("default_value"),
				)
			elif field_type == "text":
				form_data[field_name] = st.text_input(
					label, value=attributes.get("default_value")
				)
			elif field_type == "checkbox":
				form_data[field_name] = st.checkbox(
					label, value=attributes.get("default_value", False)
				)
			elif field_type == "radio":
				form_data[field_name] = st.radio(
					label,
					options=attributes.get("options"),
					index=attributes.get("options").index(
						attributes.get("default_value")
					),
				)
			elif field_type == "slider":
				form_data[field_name] = st.slider(
					label,
					min_value=attributes.get("min_value"),
					max_value=attributes.get("max_value"),
					value=attributes.get("default_value"),
				)
			elif field_type == "date":
				form_data[field_name] = st.date_input(label)
			elif field_type == "time":
				form_data[field_name] = st.time_input(label)
			elif field_type == "file":
				form_data[field_name] = st.file_uploader(label)
			elif field_type == "password":
				form_data[field_name] = st.text_input(label, type="password")
			elif field_type == "image":
				form_data[field_name] = st.image(label)
			else:
				st.warning(f"Unknown field type: {field_type}")

		# Submit button
		if st.button(self.button_label):
			# Call the model with the form data
			result = self.model(**form_data)

			# Display the result
			st.success(f"Result: {result}")
