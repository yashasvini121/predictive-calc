import pandas as pd
from sklearn.model_selection import train_test_split

# Load your dataset
try:
    df = pd.read_csv('dataset.csv')
except FileNotFoundError:
    print("Error: The file 'dataset.csv' was not found. Please check the file path.")
    exit()

# Split the data into features (X) and target (y)
X = df.drop(columns=['Churn'])  # Replace 'Churn' with the target column name if different
y = df['Churn']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Combine X and y back together for each set to save as CSV
train_data = pd.concat([X_train, y_train], axis=1)
test_data = pd.concat([X_test, y_test], axis=1)

# Save the train and test sets as separate CSV files
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)

print("Train and test datasets saved as 'train_data.csv' and 'test_data.csv'")
