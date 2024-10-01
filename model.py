import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import warnings
import pickle
import logging
from .ModelEvaluation import ModelEvaluation

warnings.filterwarnings("ignore")

# Set up logging
logging.basicConfig(
    filename='models/house_price/logs/model_training.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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
    logging.info(f"Outliers removed for features: {numerical_features}")
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
        if df[feature].nunique() == 2:
            df[feature] = pd.get_dummies(df[feature], drop_first=True, prefix=feature)
        elif 2 < df[feature].nunique() <= 16:
            df = pd.concat(
                [
                    df.drop([feature], axis=1),
                    pd.get_dummies(df[feature], drop_first=True, prefix=feature),
                ],
                axis=1,
            )
    logging.info(f"Categorical features encoded: {categorical_features}")
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
logging.info("Model training completed successfully.")

pred_train = MLR.predict(Train_X_std)
pred_test = MLR.predict(Test_X_std)

# Define RMSE logging (uncomment when evaluation is included)
# train_rmse = np.sqrt(mean_squared_error(Train_Y, pred_train))
# test_rmse = np.sqrt(mean_squared_error(Test_Y, pred_test))
# logging.info(f"Train RMSE: {train_rmse}, Test RMSE: {test_rmse}")

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

    logging.info(f"Input data prepared: {input_data}")
    return pd.DataFrame(input_data)

### Final Endpoint ###
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

    input_std = pd.DataFrame(std.transform(input_df), columns=input_df.columns)
    predicted_price = MLR.predict(input_std)

    logging.info(f"Prediction made with inputs: {input_df} | Output: {predicted_price[0]}")
    return round(predicted_price[0], 2)

def save_model():
    model_filename = "models/house_price/saved_models/model_01.pkl"
    with open(model_filename, "wb") as file:
        pickle.dump(MLR, file)
    logging.info(f"Model saved to {model_filename}")

def save_scaler():    
    scaler_filename = "models/house_price/saved_models/scaler_01.pkl"
    with open(scaler_filename, "wb") as file:
        pickle.dump(std, file)
    logging.info(f"Scaler saved to {scaler_filename}")

def get_evaluator():
    evaluator = ModelEvaluation(MLR, Train_X_std, Train_Y, Test_X_std, Test_Y)
    logging.info("Model evaluation completed")
    return evaluator
