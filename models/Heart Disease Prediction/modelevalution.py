import joblib
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

class ModelEvaluator:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions)
        print("Accuracy:", accuracy)
        print("Classification Report:\n", report)

if __name__ == "__main__":
    data = pd.read_csv('data/heart.csv')  # Load your test data
    X = data.drop('target', axis=1)  # Replace 'target' with the actual target column name
    y = data['target']  # Replace 'target' with the actual target column name

    evaluator = ModelEvaluator('saved_models/heart_disease_model.pkl')
    evaluator.evaluate(X, y)