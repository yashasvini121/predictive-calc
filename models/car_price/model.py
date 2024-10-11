# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess_data(file_path):
    # Load dataset from the provided CSV file
    df = pd.read_csv(file_path)

    # Selecting relevant columns for prediction
    relevant_columns = ['year', 'selling_price', 'km_driven', 'fuel', 'seller_type', 'transmission']
    df = df[relevant_columns]

    # Convert categorical features to numerical using LabelEncoder
    le = LabelEncoder()
    df['fuel'] = le.fit_transform(df['fuel'])
    df['seller_type'] = le.fit_transform(df['seller_type'])
    df['transmission'] = le.fit_transform(df['transmission'])

    # Define features and target variable
    X = df[['year', 'km_driven', 'fuel', 'seller_type', 'transmission']]
    y = df['selling_price']

    # Split the data into training and testing sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def train_linear_regression(X_train, y_train):
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    return lr_model

def train_lasso_regression(X_train, y_train):
    lasso_model = Lasso(alpha=0.1)
    lasso_model.fit(X_train, y_train)
    return lasso_model
