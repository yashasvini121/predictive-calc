import joblib
import pandas as pd

class CarPricePredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        return self.model.predict(input_data)

if __name__ == "__main__":
    predictor = CarPricePredictor('saved_models/car_price_model.pkl')
    
    # Example input data, replace with actual data
    # Ensure the input data has the same feature columns as used in training
    input_data = pd.DataFrame([[2015, 'Toyota', 'Corolla', 50000, 'Petrol']], 
                               columns=['year', 'company', 'model', 'kms_driven', 'fuel_type'])  # Adjust columns accordingly
    predictions = predictor.predict(input_data)
    print("Predicted Price: ₹", predictions[0])