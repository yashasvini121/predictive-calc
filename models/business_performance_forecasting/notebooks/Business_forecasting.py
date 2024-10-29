import numpy as np 
import pandas as pd 
import pickle
import os

# Load the data
df = pd.read_csv('50_Startups.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Preprocessing - Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print predictions alongside actual values
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)), axis=1))

model_path = os.path.abspath("model.pkl")
scaler_path = os.path.abspath("scaler.pkl")

# Save the model and preprocessing objects
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)

with open(scaler_path, 'wb') as scaler_file:
    pickle.dump(ct, scaler_file)

print("Model and preprocessing objects saved successfully!")
