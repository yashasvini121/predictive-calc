import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load your dataset
try:
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("Error: The file 'dataset.csv' was not found. Please check the file path.")
    exit()
# Preprocessing function
def preprocess_data(df):
    # Drop irrelevant columns if they exist
    if 'customerID' in df.columns:
        df = df.drop(columns=['customerID'])
    
    # Handle missing or invalid values in 'TotalCharges'
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].mean())
    
    # Convert 'Churn' column from 'Yes'/'No' to 1/0
    if 'Churn' in df.columns:
        df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0).astype(int)
    else:
        print("Error: 'Churn' column not found in dataset. Please check the dataset.")
        exit()
    
    # Encode other categorical features
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = LabelEncoder().fit_transform(df[col])
    
    # Scale numerical features
    scaler = StandardScaler()
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
    
    return df

# Apply the preprocessing to the data
df = preprocess_data(df)

# Apply preprocessing
df = preprocess_data(df)

# Split data into features and target
X = df.drop(columns=['Churn'])
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)

# Performance metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Display results
print("Model Performance:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Feature Importance
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nFeature Importances:\n", feature_importances)

# Save feature importance as a CSV file
feature_importances.to_csv('feature_importances.csv', index=True)
