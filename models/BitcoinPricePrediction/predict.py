import joblib
import pandas as pd

class LoanApprovalPredictor:
    def __init__(self, model_path, scaler_path):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def predict(self, input_data):
        input_data_scaled = self.scaler.transform(input_data)
        return self.model.predict(input_data_scaled)

if __name__ == "__main__":
    predictor = LoanApprovalPredictor('saved_models/model.pkl', 'saved_models/scaler.pkl')
    # Example input data, replace with actual data
    input_data = pd.DataFrame([[...]], columns=[...])  # Replace with actual column names
    predictions = predictor.predict(input_data)
    print(predictions)