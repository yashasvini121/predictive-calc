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
    input_data = pd.DataFrame([[...]], columns=[...])  # Replace with actual column names
    predictions = predictor.predict(input_data)
    print(predictions)