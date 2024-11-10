# predict.py

import joblib
import pandas as pd
from URLFeatureExtraction import featureExtraction  # Make sure this is the correct import path

def predict(url):
    # Load the trained model
    model = joblib.load('phishing_model.pkl')

    # Extract features from the URL
    features = featureExtraction(url)

    # Convert features to DataFrame for prediction
    features_df = pd.DataFrame([features], columns=[
        'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection', 
        'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 
        'Web_Traffic', 'Domain_Age', 'Domain_End', 
        'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards'
    ])

    # Make prediction
    prediction = model.predict(features_df)

    return "Phishing" if prediction[0] == 1 else "Legitimate"

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    result = predict(url)
    print(f"The URL is: {result}")