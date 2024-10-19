# from models.insurance_cost_predictor.model import insurance_cost_prediction
from model import insurance_cost_prediction


def get_prediction(age, sex, bmi, children, smoker, region):
    # Call the function that makes the insurance cost prediction using input features
    return insurance_cost_prediction(age, sex, bmi, children, smoker, region)
