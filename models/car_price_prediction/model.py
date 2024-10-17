# model.py

# Data manipulation and processing
import pandas as pd
import numpy as np

# Machine Learning models
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('data/car_data.csv')

# Data preprocessing
df['mileage(km/ltr/kg)'] = pd.to_numeric(df['mileage(km/ltr/kg)'], errors='coerce')
df['engine'] = pd.to_numeric(df['engine'], errors='coerce')
df['max_power'] = pd.to_numeric(df['max_power'], errors='coerce')
df['seats'] = pd.to_numeric(df['seats'], errors='coerce')

# Fill missing values for specific columns with their median
df['mileage(km/ltr/kg)'].fillna(df['mileage(km/ltr/kg)'].median(), inplace=True)
df['engine'].fillna(df['engine'].median(), inplace=True)
df['max_power'].fillna(df['max_power'].median(), inplace=True)
df['seats'].fillna(df['seats'].median(), inplace=True)

# Calculate the car's age
df['age'] = 2024 - df['year']
df.drop(columns=['year'], inplace=True)

# One-hot encode the categorical columns
df = pd.get_dummies(df, columns=['fuel', 'seller_type', 'transmission', 'owner'], drop_first=True)
df.drop(columns=['name'], inplace=True)

# Scale the features
features_to_scale = ['km_driven', 'mileage(km/ltr/kg)', 'engine', 'max_power', 'seats', 'age']
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Define features (X) and target (y)
X = df.drop(columns=['selling_price'])
y = df['selling_price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# Train Lasso Regression model with hyperparameter tuning
lasso_cv = GridSearchCV(Lasso(), {'alpha': np.logspace(-4, 0, 50)}, cv=5)
lasso_cv.fit(X_train, y_train)
best_alpha = lasso_cv.best_params_['alpha']
lasso_reg = Lasso(alpha=best_alpha)
lasso_reg.fit(X_train, y_train)

# Save models and scaler for later use
import joblib
joblib.dump(lin_reg, 'models/linear_regression_model.pkl')
joblib.dump(lasso_reg, 'models/lasso_regression_model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')

print('Models trained and saved successfully.')
