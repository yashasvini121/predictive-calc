import joblib
import numpy as np


model = joblib.load('saved_models/Gradient_Boosting_Classifier.joblib')
scaler = joblib.load('saved_models/scaler.joblib')

def get_user_input():
    features = {}
    features['CreditScore'] = int(input("Enter Credit Score: "))
    features['Geography'] = input("Enter Geography (France/Spain/Germany): ")
    features['Gender'] = input("Enter Gender (Male/Female): ")
    features['Age'] = int(input("Enter Age: "))
    features['Tenure'] = int(input("Enter Tenure: "))
    features['Balance'] = float(input("Enter Balance: "))
    features['NumOfProducts'] = int(input("Enter Number of Products: "))
    features['HasCrCard'] = int(input("Has Credit Card? (1 for Yes, 0 for No): "))
    features['IsActiveMember'] = int(input("Is Active Member? (1 for Yes, 0 for No): "))
    features['EstimatedSalary'] = float(input("Enter Estimated Salary: "))
    return features

def preprocess_input(features):
    geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
    gender_map = {'Female': 0, 'Male': 1}
    
    features['Geography'] = geography_map[features['Geography']]
    features['Gender'] = gender_map[features['Gender']]
    input_array = np.array(list(features.values())).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    
    return scaled_input

def predict_churn(features):
    
    preprocessed_input = preprocess_input(features)
    prediction = model.predict(preprocessed_input)
    probability = model.predict_proba(preprocessed_input)[0][1]
    print(prediction)
    return prediction[0], probability

if __name__ == "__main__":
    print("Welcome to the Customer Churn Predictor")
    user_input = get_user_input()
    prediction, probability = predict_churn(user_input)
    
    if prediction == 1:
        print(f"The customer is likely to churn with a probability of {probability:.2f}")
    else:
        print(f"The customer is likely to stay with a probability of {1-probability:.2f}")




