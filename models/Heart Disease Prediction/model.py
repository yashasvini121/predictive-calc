import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

class HeartDiseaseModel:
    def __init__(self):
        self.model = RandomForestClassifier(random_state=42)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        return data

    def preprocess_data(self, data):
        # Assuming 'target' is the column indicating heart disease presence
        X = data.drop('target', axis=1)  # Replace 'target' with the actual target column name
        y = data['target']  # Replace 'target' with the actual target column name
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

if __name__ == "__main__":
    model = HeartDiseaseModel()
    data = model.load_data('data/heart_disease_data.csv')  # Adjust the path to your dataset
    X_train, X_test, y_train, y_test = model.preprocess_data(data)
    model.train(X_train, y_train)
    model.save_model('saved_models/heart_disease_model.pkl')