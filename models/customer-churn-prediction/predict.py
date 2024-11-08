import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the test dataset
try:
    test_df = pd.read_csv('data/test_data.csv')
except FileNotFoundError:
    print("Error: The file 'test_data.csv' was not found. Please check the file path.")
    exit()

# Preprocessing function (reused, but loading scaler instead of fitting)
def preprocess_data(df, is_train=False):
    # Drop irrelevant columns if they exist
    if 'customerID' in df.columns:
        df = df.drop(columns=['customerID'])
    
    # Handle missing or invalid values in 'TotalCharges'
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())
    
    # Convert 'Churn' column from 'Yes'/'No' to 1/0 if present
    if 'Churn' in df.columns:
        df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0).astype(int)
    
    # Encode other categorical features
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = LabelEncoder().fit_transform(df[col])
    
    # Load the scaler and scale numerical features
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_columns] = scaler.transform(df[numerical_columns])
    
    return df

# Preprocess test data
test_df = preprocess_data(test_df)

# Split data into features and target
X_test = test_df.drop(columns=['Churn'])
y_test = test_df['Churn']

# Load the saved model
with open('saved_models/random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)
print("Model loaded for prediction")

# Make predictions
y_pred = model.predict(X_test)

# Display predictions and accuracy
print("Predictions:", y_pred)

# Calculate and print metrics if you want
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\nModel Performance on Test Data:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
