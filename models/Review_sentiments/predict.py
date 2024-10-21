# models/tweet_sentiment_analysis/predict.py

import joblib
import pandas as pd

# Load the model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict_sentiment(tweet):
    # Transform the input tweet
    tweet_vectorized = vectorizer.transform([tweet])
    
    # Make prediction
    prediction = model.predict(tweet_vectorized)[0]
    
    return "Positive" if prediction == 1 else "Negative"
