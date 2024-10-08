import joblib
import numpy as np
model = joblib.load('models/Customer_Churn_Prediction/saved_models/Gradient_Boosting_Classifier.joblib')
scaler = joblib.load('models/Customer_Churn_Prediction/saved_models/scaler.joblib')
def customer_churn_prediction(cs,geo,gen,age,tenure,bal,nop,hcc,iam,es):
    features = {'CreditScore':cs,'Geography':geo,'Gender':gen,'Age':age,'Tenure':tenure,'Balance':bal,'NumOfProducts':nop,'HasCrCard':hcc,'IsActiveMember':iam,'EstimatedSalary':es}
    geography_map = {'France': 0, 'Spain': 1, 'Germany': 2}
    gender_map = {'Female': 0, 'Male': 1}
    features['Geography'] = geography_map[features['Geography']]
    features['Gender'] = gender_map[features['Gender']]
    input_array = np.array(list(features.values())).reshape(1, -1)
    scaled_input = scaler.transform(input_array)
    preprocessed_input = scaled_input
    prediction = model.predict(preprocessed_input)
    probability = model.predict_proba(preprocessed_input)[0][1]
    print(prediction)
    return prediction[0], probability