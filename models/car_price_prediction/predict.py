# predict.py

import pandas as pd
import joblib

# Load the models and scaler
lin_reg = joblib.load('models/linear_regression_model.pkl')
lasso_reg = joblib.load('models/lasso_regression_model.pkl')
scaler = joblib.load('models/scaler.pkl')

# Features to scale
features_to_scale = ['km_driven', 'mileage(km/ltr/kg)', 'engine', 'max_power', 'seats', 'age']

# Function to predict the selling price
def predict_price(year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats):
    # Calculate the car's age
    age = 2024 - year

    # Create a DataFrame for input
    input_data = pd.DataFrame({
        'km_driven': [km_driven],
        'mileage(km/ltr/kg)': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'seats': [seats],
        'age': [age],
        'fuel_Diesel': [1 if fuel == 'Diesel' else 0],
        'fuel_LPG': [1 if fuel == 'LPG' else 0],
        'fuel_Petrol': [1 if fuel == 'Petrol' else 0],
        'seller_type_Individual': [1 if seller_type == 'Individual' else 0],
        'seller_type_Trustmark Dealer': [1 if seller_type == 'Trustmark Dealer' else 0],
        'transmission_Manual': [1 if transmission == 'Manual' else 0],
        'owner_Fourth & Above Owner': [1 if owner == 'Fourth & Above Owner' else 0],
        'owner_Second Owner': [1 if owner == 'Second Owner' else 0],
        'owner_Test Drive Car': [1 if owner == 'Test Drive Car' else 0],
        'owner_Third Owner': [1 if owner == 'Third Owner' else 0]
    })

    # Scale the features using the previously fitted scaler
    input_data[features_to_scale] = scaler.transform(input_data[features_to_scale])

    # Predict using both models
    predicted_price_linear = lin_reg.predict(input_data)[0]
    predicted_price_lasso = lasso_reg.predict(input_data)[0]

    return predicted_price_linear, predicted_price_lasso

# Example inputs for prediction
if __name__ == '__main__':
    year = int(input("Enter car year: "))
    km_driven = float(input("Enter kilometers driven: "))
    fuel = input("Enter fuel type (Diesel/LPG/Petrol): ")
    seller_type = input("Enter seller type (Individual/Trustmark Dealer): ")
    transmission = input("Enter transmission type (Manual/Automatic): ")
    owner = input("Enter owner type (First/Second/Third/Fourth & Above/Test Drive Car): ")
    mileage = float(input("Enter mileage (km/ltr): "))
    engine = float(input("Enter engine size (cc): "))
    max_power = float(input("Enter max power (bhp): "))
    seats = int(input("Enter number of seats: "))

    # Get predictions
    predicted_price_linear, predicted_price_lasso = predict_price(year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats)

    # Print the predicted prices
    print(f"Predicted Selling Price (Linear Regression): {predicted_price_linear:.2f}")
    print(f"Predicted Selling Price (Lasso Regression): {predicted_price_lasso:.2f}")
