import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pickle

def load_data(file_path):
    data = pd.read_csv(file_path)
    data.replace('?', np.nan, inplace=True)
    data = data.apply(pd.to_numeric, errors='coerce')
    return data

def preprocess_data(data):
    X = data.drop(columns=['Dx'])
    y = data['Dx']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X_scaled)
    return X_imputed, y, scaler, imputer

def train_model(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

if __name__ == "__main__":
    data = load_data('models/cervical_cancer/data/kag_risk_factors_cervical_cancer.csv')
    X, y, scaler, imputer = preprocess_data(data)
    model = train_model(X, y)

    with open('models/cervical_cancer/saved_models/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('models/cervical_cancer/saved_models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
