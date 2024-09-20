import pickle
import pandas as pd

def load_model(filepath):
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
	# Creates a dictionary for the input features
	input_data = {
		"area": [area],
		"mainroad": True if mainroad == "Yes" else False,
		"guestroom": True if guestroom == "Yes" else False,
		"basement": True if basement == "Yes" else False,
		"hotwaterheating": True if hotwaterheating == "Yes" else False,
		"airconditioning": True if airconditioning == "Yes" else False,
		"prefarea": True if prefarea == "Yes" else False,
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


### Final Endpoint ###
# Predicts the price of a house based on the input features
def house_price_prediction_model(
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
	# Modifying the input data to match the model's input format
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
	scaled_df = pd.DataFrame(
		input_scaled, columns=scaler.get_feature_names_out()
	)  # Did this to get correct feature names (was getting the warning UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names ...)

	# Predict the house price
	predicted_price = model.predict(scaled_df)

	return round(predicted_price[0], 2)

### Test ###
def test_house_price_prediction():
    # Sample inputs
    area = 3000
    mainroad = "Yes"
    guestroom = "No"
    basement = "Yes"
    hotwaterheating = "No"
    airconditioning = "Yes"
    prefarea = "Yes"
    bedrooms = 2
    bathrooms = 3
    stories = 2
    parking = 2
    furnishingstatus = "semi_furnished"

    predicted_price = house_price_prediction_model(
		area=area,
		mainroad=mainroad,
		guestroom=guestroom,
		basement=basement,
		hotwaterheating=hotwaterheating,
		airconditioning=airconditioning,
		prefarea=prefarea,
		bedrooms=bedrooms,
		bathrooms=bathrooms,
		stories=stories,
		parking=parking,
		furnishingstatus=furnishingstatus,
	)

    print("Predicted House Price: Rs.", predicted_price)


test_house_price_prediction()
