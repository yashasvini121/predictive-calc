import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pickle

# Load the training dataset
try:
    train_df = pd.read_csv('data/train_data.csv')
except FileNotFoundError:
    print("Error: The file 'train_data.csv' was not found. Please check the file path.")
    exit()

# Preprocessing function
def preprocess_data(df, is_train=True):
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
    
    # Encode other categorical features
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        df[col] = LabelEncoder().fit_transform(df[col])
    
    # Scale numerical features
    scaler = StandardScaler()
    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    if is_train:
        df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
        with open('scaler.pkl', 'wb') as f:
            pickle.dump(scaler, f)  # Save the scaler for consistent scaling in testing
    else:
        df[numerical_columns] = scaler.transform(df[numerical_columns])
    
    return df

# Preprocess training data
train_df = preprocess_data(train_df)

# Split data into features and target
X_train = train_df.drop(columns=['Churn'])
y_train = train_df['Churn']

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a .pkl file
with open('saved_models/random_forest_model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model has been trained and saved as 'random_forest_model.pkl'")
