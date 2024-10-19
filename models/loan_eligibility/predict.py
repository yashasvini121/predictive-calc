from models.loan_eligibility.model import loan_approval_prediction

def get_prediction(no_of_dependents, education, self_employed, income_annum, loan_amount,
                   loan_term, cibil_score, residential_assets_value, commercial_assets_value,
                   luxury_assets_value, bank_asset_value):
    
    # Use the loan_approval_prediction function to get the result
    prediction = loan_approval_prediction(no_of_dependents, education, self_employed, income_annum, loan_amount,
                                          loan_term, cibil_score, residential_assets_value, commercial_assets_value,
                                          luxury_assets_value, bank_asset_value)

    if prediction == 0:
        prediction = 'APPROVED !'
    else:
        prediction = 'REJECTED'

    return prediction
