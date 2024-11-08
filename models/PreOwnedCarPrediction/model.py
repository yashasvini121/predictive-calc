import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

class CarPriceModel:
    def __init__(self):
        self.model = LinearRegression()

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        return data

    def preprocess_data(self, data):
        # Perform preprocessing steps here
        X = data.drop('price', axis=1)  # Assuming 'price' is the target column
        y = data['price']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def save_model(self, model_path):
        joblib.dump(self.model, model_path)

if __name__ == "__main__":
    car_model = CarPriceModel()
    data = car_model.load_data('data/car_data.csv')  # Example path
    X_train, X_test, y_train, y_test = car_model.preprocess_data(data)
    car_model.train(X_train, y_train)
    car_model.save_model('saved_models/car_price_model.pkl')