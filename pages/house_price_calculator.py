import streamlit as st
from form_handler import FormHandler
from models.house_price.predict import house_price_prediction_model, model_details

# Page Title
st.title("House Price Prediction Calculator")

# Creates the form with FormHandler, using the field mappings
house_form = FormHandler(
	name="House Price Estimator",
	button_label="Predict Price",
	model=house_price_prediction_model,
	config_path="form_configs/house_price.json",
)

# Create tabs for the calculator and model details
tabs = st.tabs(["Calculator", "Model Details"])

# Renders the calculator in the first tab
with tabs[0]:
	house_form.render()


metrics, prediction_plot, error_plot = model_details().evaluate()

# Renders model details in the second tab
with tabs[1]:
	st.header("Model Details")
	st.subheader(
		f"Model Accuracy: {metrics['Test_R2']:.2%}"
	)
	st.subheader(
		f"Scores: {metrics['Train_R2']:.2f}, {metrics['Test_R2']:.2f}"
	)

	# Displays scatter plot for actual vs predicted
	st.subheader("Plots")
	st.pyplot(prediction_plot)

	# todo: fix this, both the error_plot and performance_plot are combined
	
	# Displays error terms plot
	# st.subheader("Error Terms Distribution")
	# st.pyplot(error_plot)

	# Displays performance comparison graph
	# st.subheader("Model Performance Graph")
	# performance_plot = model_details().plot_performance_graph()
	# st.pyplot(performance_plot)
