import pandas as pd
import pickle
from models.customer_income.model import predict

def load_model():
    with open('models/customer_income/saved_models/feature_names.pkl', 'rb') as feature_file:
        feature_names = pickle.load(feature_file)
    return feature_names

def get_prediction(age, workclass, fnlwgt, education, marital_status, relationship, occupation, sex, race, capital_gain, capital_loss, hours_per_week, native_country):
    input_dict = {
        'age': age,
        'fnlwgt': fnlwgt,
        'capital-gain': capital_gain,  
        'capital-loss': capital_loss,
        'hours-per-week': hours_per_week,
        'workclass_' + workclass: 1,
        'education_' + education: 1,
        'marital-status_' + marital_status: 1,
        'relationship_' + relationship: 1,
        'occupation_' + occupation: 1,
        'sex_' + sex: 1,
        'race_' + race: 1,
        'native-country_' + native_country: 1,
    }

    feature_names = load_model()
    
    input_df = pd.DataFrame(0, index=[0], columns=feature_names)
    
    for key, value in input_dict.items():
        if key in input_df.columns:
            input_df[key] = value
        else:
            print(f"Warning: {key} not found in feature columns.")
    

    result = predict(input_df)

    if result == 1:
        return "The person earns more than 50,000$ per year."
    else:
        return "The person earns less than or equal to 50,000$ per year."
