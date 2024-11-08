import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

class ModelEvaluator:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print("Mean Squared Error:", mse)
        print("R^2 Score:", r2)

if __name__ == "__main__":
    data = pd.read_csv('data/car_data.csv')  # Load your test data
    X_test = data.drop('price', axis=1)  # Adjust based on your dataset
    y_test = data['price']
    evaluator = ModelEvaluator('saved_models/car_price_model.pkl')
    evaluator.evaluate(X_test, y_test)