import streamlit as st
import json
from typing import Dict, Any, Optional

class FormHandler:
    """
    A class to handle rendering a form in Streamlit based on a configuration file.
    
    Attributes:
        name (str): The name of the form to be rendered.
        button_label (str): The label for the submit button.
        model (callable): The model function to be called with form data.
        config_path (str): Path to the configuration JSON file.
        field_mappings (Dict[str, str]): Mapping of form field names to model-compatible names.
    """
    
    def __init__(
        self,
        name: str,
        button_label: str,
        model: callable,
        config_path: str,
        field_mappings: Optional[Dict[str, str]] = None,
    ) -> None:
        """
        Initializes the FormHandler with the provided parameters.
        
        Parameters:
            name (str): The name of the form to be rendered.
            button_label (str): The label for the submit button.
            model (callable): The model function to be called with form data.
            config_path (str): Path to the configuration JSON file. Default is "config/config.json".
            field_mappings (Optional[Dict[str, str]]): Mapping of form field names to model-compatible names. Default is None.
        """
        self.name = name
        self.button_label = button_label
        self.model = model
        self.config_path = config_path
        self.fields = self.load_fields_from_config()
        self.field_mappings = field_mappings or {}

    def load_fields_from_config(self) -> Dict[str, Dict[str, Any]]:
        """
        Loads form fields from the configuration JSON file.
        
        Returns:
            Dict[str, Dict[str, Any]]: A dictionary of form fields and their attributes.
        """
        with open(self.config_path, "r") as f:
            config = json.load(f)
        return config.get(self.name, {})

    def render(self) -> None:
        """
        Renders the form in the Streamlit application.
        
        This method collects user input and, upon form submission, calls the specified model 
        with the collected data mapped to the appropriate field names.
        """
        # Dictionary to hold form data
        form_data: Dict[str, Any] = {}

        # Loop over the fields in the form
        for label, attributes in self.fields.items():
            field_type = attributes.get("type")

            # Handle different types of input fields
            if field_type == "number":
                form_data[label] = st.number_input(
                    label,
                    value=attributes.get("default_value"),
                    min_value=attributes.get("min_value"),
                    max_value=attributes.get("max_value"),
                    step=attributes.get("step", 1),
                )
            elif field_type == "dropdown":
                form_data[label] = st.selectbox(
                    label,
                    options=attributes.get("options"),
                    index=attributes.get("options").index(
                        attributes.get("default_value")
                    ),
                )
            elif field_type == "range":
                form_data[label] = st.slider(
                    label,
                    min_value=attributes.get("min_value"),
                    max_value=attributes.get("max_value"),
                    value=tuple(attributes.get("default_value")),  # type: ignore
                )
            elif field_type == "multiselect":
                form_data[label] = st.multiselect(
                    label,
                    options=attributes.get("options"),
                    default=attributes.get("default_value"),
                )
            elif field_type == "text":
                form_data[label] = st.text_input(
                    label, value=attributes.get("default_value")
                )
            elif field_type == "checkbox":
                form_data[label] = st.checkbox(
                    label, value=attributes.get("default_value", False)
                )
            elif field_type == "radio":
                form_data[label] = st.radio(
                    label,
                    options=attributes.get("options"),
                    index=attributes.get("options").index(
                        attributes.get("default_value")
                    ),
                )

        # Submit button
        if st.button(self.button_label):
            # Map the form_data to model-compatible field names using field_mappings

            mapped_data = {
                self.field_mappings.get(key, key): value
                for key, value in form_data.items()
            }

            result = self.model(**mapped_data)
            
            # Rounds the result to 2 decimal places
            st.success(f"Result: {result:.2f}")
