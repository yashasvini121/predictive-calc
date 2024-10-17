import pandas as pd
import joblib

class DiabetesModel:
    def __init__(self, model_path: str):
        # Ensure the model file exists and is correctly loaded
        try:
            self.model = joblib.load(model_path)
        except FileNotFoundError:
            print(f"Error: Model file not found at {model_path}")
            self.model = None  # Set to None if the file is missing

    def preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        # Perform necessary preprocessing steps, e.g., encoding, scaling
        # Example: Convert categorical variables, handle missing values, etc.
        age_bins = {'10-20': 0, '20-30': 1, '30-40': 2, '40-50': 3, '50-60': 4, '60-70': 5, '70-80': 6, '80+': 7}
        data['age'] = data['age'].map(age_bins)
        return data

    def predict(self, input_data: dict) -> int:
        # Convert input_data to DataFrame
        input_df = pd.DataFrame([input_data])
        processed_data = self.preprocess(input_df)
        prediction = self.model.predict(processed_data)
        return "No" if prediction[0] == 0 else "Yes"


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def model_details(model, model_name: str, X_train_selected, y_train, X_test_selected, y_test) -> None:
    """
    Prints detailed information about the machine learning model, its performance on training and testing data, 
    and other relevant evaluation metrics.
    
    Parameters:
    - model: Trained model object (e.g., RandomForestClassifier, LogisticRegression, etc.)
    - model_name: Name of the model as a string (e.g., "Random Forest Classifier")
    - X_train: Training features dataset
    - y_train: Training target dataset
    - X_test: Testing features dataset
    - y_test: Testing target dataset
    """

    # Model name and hyperparameters
    print(f"Model Name: {model_name}")
    print("\nModel Hyperparameters:")
    print(model.get_params())

    # Training accuracy
    train_score = model.score(X_train_selected, y_train)
    print(f"\nTraining Accuracy: {train_score:.4f}")

    # Testing accuracy
    test_score = model.score(X_test_selected, y_test)
    print(f"Testing Accuracy: {test_score:.4f}")

    # Predictions on test data
    y_pred = model.predict(X_test_selected)

    # Detailed classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Confusion matrix
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Additional evaluation metrics
    acc_score = accuracy_score(y_test, y_pred)
    print(f"\nOverall Accuracy Score: {acc_score:.4f}")

    # If additional metrics like F1-score, Precision, or Recall are needed, you can also calculate them here
    # Example: f1_score, precision_score, recall_score from sklearn.metrics can be included if necessary.

