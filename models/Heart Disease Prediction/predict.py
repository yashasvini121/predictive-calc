import joblib
import pandas as pd

class HeartDiseasePredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, input_data):
        return self.model.predict(input_data)

if __name__ == "__main__":
    predictor = HeartDiseasePredictor('saved_models/heart_disease_model.pkl')
    
    # Example input data, replace with actual data
    # Ensure the input data has the same feature columns as used in training
    input_data = pd.DataFrame([[63, 1, 3, 145, 233, 1, 0, 2]],  # Example input
                               columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'])  # Adjust columns accordingly

    predictions = predictor.predict(input_data)
    print("Predicted Heart Disease Presence:", "Yes" if predictions[0] == 1 else "No")