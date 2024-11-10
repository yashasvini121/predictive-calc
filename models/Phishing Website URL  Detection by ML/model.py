# model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def train_model(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)

    # Split the data into features and target
    X = data.drop(columns=['Label'])  # Assuming 'Label' is the target column
    y = data['Label']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Save the model as a .pkl file
    joblib.dump(model, 'phishing_model.pkl')

if __name__ == "__main__":
    train_model('data.csv')  # Replace with your dataset path