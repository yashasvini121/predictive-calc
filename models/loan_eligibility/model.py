import joblib

with open('models/loan_eligibility/saved_models/knn_model.joblib', 'rb') as file:
    model = joblib.load(file)
    
def loan_approval_prediction(no_of_dependents, education, self_employed, income_annum, loan_amount,
                             loan_term, cibil_score, residential_assets_value, commercial_assets_value,
                             luxury_assets_value, bank_asset_value):
    # Feature extraction
    if education == "Graduate":
        education = 0
    else:
        education = 1

    if self_employed == "No":
        self_employed = 0
    else:
        self_employed = 1

    # Calculate derived features
    monthly_gross_income = income_annum / 12
    monthly_debt_payments = loan_amount / (loan_term * 12)
    dti_ratio = monthly_debt_payments / monthly_gross_income
    total_assets = residential_assets_value + commercial_assets_value + luxury_assets_value + bank_asset_value
    asset_to_loan_ratio = total_assets / loan_amount
    net_worth = total_assets - loan_amount

    # Create a feature list for prediction
    features = [
        int(no_of_dependents),
        int(education),
        int(self_employed),
        float(income_annum),
        float(loan_amount),
        float(loan_term),
        int(cibil_score),
        float(residential_assets_value),
        float(commercial_assets_value),
        float(luxury_assets_value),
        float(bank_asset_value),
        float(dti_ratio),
        float(asset_to_loan_ratio),
        float(net_worth)
    ]

    # Make a prediction using the model
    prediction = model.predict([features])[0]
    
    return prediction
