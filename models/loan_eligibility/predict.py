from models.loan_eligibility.model import loan_eligibility

def get_prediction(income, loan_amount, credit_score):
	return loan_eligibility(income, loan_amount, credit_score)