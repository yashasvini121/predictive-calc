import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

class LoanApprovalModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.scaler = StandardScaler()

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        return data

    def preprocess_data(self, data):
        # Perform preprocessing steps here
        X = data.drop('target', axis=1)
        y = data['target']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self, X_train, y_train):
        self.scaler.fit(X_train)
        X_train_scaled = self.scaler.transform(X_train)
        self.model.fit(X_train_scaled, y_train)

    def save_model(self, model_path, scaler_path):
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)

if __name__ == "__main__":
    loan_model = LoanApprovalModel()
    data = loan_model.load_data('data/loan_data.csv')  # Example path
    X_train, X_test, y_train, y_test = loan_model.preprocess_data(data)
    loan_model.train(X_train, y_train)
    loan_model.save_model('saved_models/model.pkl', 'saved_models/scaler.pkl')