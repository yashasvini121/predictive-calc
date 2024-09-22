import pickle
import pandas as pd
from models.house_price.model import get_evaluator

"""
Predict.py file:
Contains the following functions:
- load_model: Loads a model from a pickle file.
- prepare_input_data: Prepares the input data for the model.
- [IMPORTANT] get_prediction: Predicts the price of a house based on the input features.
- test_house_price_prediction: Tests the house price prediction model.
- [IMPORTANT] model_details: Returns the details of the model.
"""


def load_model(filepath):
	"""Loads a model from the given pickle file path."""
	with open(filepath, "rb") as file:
		model = pickle.load(file)
	return model


def prepare_input_data(
	area,
	mainroad,
	guestroom,
	basement,
	hotwaterheating,
	airconditioning,
	prefarea,
	additional_bedrooms,
	bathrooms,
	stories,
	parking,
	furnishingstatus,
):
	"""
	Prepares the input data for the model by converting user inputs into a
	structured DataFrame format.
	"""
	input_data = {
		"area": [area],
		"mainroad": mainroad == "Yes",
		"guestroom": guestroom == "Yes",
		"basement": basement == "Yes",
		"hotwaterheating": hotwaterheating == "Yes",
		"airconditioning": airconditioning == "Yes",
		"prefarea": prefarea == "Yes",
		"bedrooms_2": additional_bedrooms == 2,
		"bedrooms_3": additional_bedrooms == 3,
		"bedrooms_4": additional_bedrooms == 4,
		"bedrooms_5": additional_bedrooms == 5,
		"bedrooms_6": additional_bedrooms == 6,
		"bathrooms_2": bathrooms == 2,
		"bathrooms_3": bathrooms == 3,
		"bathrooms_4": bathrooms == 4,
		"stories_2": stories == 2,
		"stories_3": stories == 3,
		"stories_4": stories == 4,
		"parking_1": parking == 1,
		"parking_2": parking == 2,
		"parking_3": parking == 3,
		"furnishingstatus_semi_furnished": furnishingstatus == "semi_furnished",
		"furnishingstatus_unfurnished": furnishingstatus == "unfurnished",
	}

	return pd.DataFrame(input_data)


def get_prediction(
	area=0,
	mainroad=False,
	guestroom=False,
	basement=False,
	hotwaterheating=False,
	airconditioning=False,
	prefarea=False,
	bedrooms=0,
	bathrooms=2,
	stories=1,
	parking=1,
	furnishingstatus="semi_furnished",
):
	"""
	Predicts the house price based on the input features.
	Returns the predicted house price rounded to two decimal places.
	"""
	# Prepare input data
	input_df = prepare_input_data(
		area,
		mainroad,
		guestroom,
		basement,
		hotwaterheating,
		airconditioning,
		prefarea,
		bedrooms,
		bathrooms,
		stories,
		parking,
		furnishingstatus,
	)

	# Load the model and the scaler
	model = load_model("models/house_price/saved_models/model_01.pkl")
	scaler = load_model("models/house_price/saved_models/scaler_01.pkl")

	# Scale the input data
	input_scaled = scaler.transform(input_df)
	scaled_df = pd.DataFrame(input_scaled, columns=scaler.get_feature_names_out())

	# Predict the house price
	predicted_price = model.predict(scaled_df)

	return round(predicted_price[0], 2)


def test_house_price_prediction():
	"""Test function to predict a sample house price."""
	# Sample inputs
	sample_input = {
		"area": 3000,
		"mainroad": "Yes",
		"guestroom": "No",
		"basement": "Yes",
		"hotwaterheating": "No",
		"airconditioning": "Yes",
		"prefarea": "Yes",
		"bedrooms": 2,
		"bathrooms": 3,
		"stories": 2,
		"parking": 2,
		"furnishingstatus": "semi_furnished",
	}

	predicted_price = get_prediction(**sample_input)

	print("Predicted House Price: Rs.", predicted_price)


def model_details():
	"""Returns model evaluation details."""
	return get_evaluator()
