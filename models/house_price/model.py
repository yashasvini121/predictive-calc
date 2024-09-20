import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import warnings
import pickle
from ModelEvaluation import ModelEvaluation

warnings.filterwarnings("ignore")

df = pd.read_csv("models/house_price/data/housing.csv")
original_df = df.copy(deep=True)

# Target and Feature Identification
target = "price"
features = [col for col in df.columns if col != target]

# Separates numerical and categorical features based on unique values
nu = df[features].nunique()
numerical_features = [col for col in features if nu[col] > 16]
categorical_features = [col for col in features if nu[col] <= 16]

# Removing outliers using IQR
def remove_outliers(df, numerical_features):
	for feature in numerical_features:
		Q1 = df[feature].quantile(0.25)
		Q3 = df[feature].quantile(0.75)
		IQR = Q3 - Q1
		df = df[(df[feature] >= (Q1 - 1.5 * IQR)) & (df[feature] <= (Q3 + 1.5 * IQR))]
	return df.reset_index(drop=True)


# Handling missing values
def handle_missing_values(df):
	null_summary = df.isnull().sum()
	null_percentage = (null_summary / df.shape[0]) * 100
	return pd.DataFrame(
		{"Total Null Values": null_summary, "Percentage": null_percentage}
	).sort_values(by="Percentage", ascending=False)


# Removes outliers from numerical features
df = remove_outliers(df, numerical_features)

# Filters categorical features without missing values
null_value_summary = handle_missing_values(df)
valid_categorical_features = [
	col
	for col in categorical_features
	if col not in null_value_summary[null_value_summary["Percentage"] != 0].index
]

# Encoding categorical features
def encode_categorical_features(df, categorical_features):
	for feature in categorical_features:
		# Binary encoding for features with 2 unique values
		if df[feature].nunique() == 2:
			df[feature] = pd.get_dummies(df[feature], drop_first=True, prefix=feature)
		# Dummy encoding for features with more than 2 unique values
		elif 2 < df[feature].nunique() <= 16:
			df = pd.concat(
				[
					df.drop([feature], axis=1),
					pd.get_dummies(df[feature], drop_first=True, prefix=feature),
				],
				axis=1,
			)
	return df

df = encode_categorical_features(df, valid_categorical_features)

# Renames columns to avoid invalid characters
df.columns = [col.replace("-", "_").replace(" ", "_") for col in df.columns]

# Splitting the data into training & testing sets
X = df.drop([target], axis=1)
Y = df[target]
Train_X, Test_X, Train_Y, Test_Y = train_test_split(
	X, Y, train_size=0.8, test_size=0.2, random_state=100
)

# Feature Scaling (Standardization)
std = StandardScaler()
Train_X_std = pd.DataFrame(std.fit_transform(Train_X), columns=X.columns)
Test_X_std = pd.DataFrame(std.transform(Test_X), columns=X.columns)

# Multiple Linear Regression with sklearn
MLR = LinearRegression().fit(Train_X_std, Train_Y)
pred_train = MLR.predict(Train_X_std)
pred_test = MLR.predict(Test_X_std)

# Calculate RMSE for train and test sets
# train_rmse = np.sqrt(mean_squared_error(Train_Y, pred_train))
# test_rmse = np.sqrt(mean_squared_error(Test_Y, pred_test))


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

# Note: Not removing this fxn because of the warning in predict.py file

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

	# Standardizes the input data
	input_std = pd.DataFrame(std.transform(input_df), columns=input_df.columns)

	# Predicts the price
	predicted_price = MLR.predict(input_std)

	return round(predicted_price[0], 2)


def save_model():
	# todo: Ask the user for the model name, and warn that the model will be overwritten
	
	with open("models/house_price/saved_models/model_01.pkl", "wb") as file:
		pickle.dump(MLR, file)


def save_scaler():    
	with open("models/house_price/saved_models/scaler_01.pkl", "wb") as file:
		pickle.dump(std, file)


def model_evaluation():
	me = ModelEvaluation(MLR, Train_X_std, Train_Y, Test_X_std, Test_Y)
	me.evaluate()


# if __name__ == "__main__":
	# save_model()
	# save_scaler()
	# model_evaluation()