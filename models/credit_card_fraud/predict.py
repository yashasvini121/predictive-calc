import pandas as pd
import pickle
from models.credit_card_fraud.model import  get_evaluator


def load_model(model_path):
    """ Load the trained Random Forest model from the specified path. """
    with open(model_path, 'rb') as file:
        return pickle.load(file)


def prepare_input_data(
        avg_amount_per_day,
        transaction_amount,
        Is_declined,
        no_of_declines_per_day,
        Is_Foreign_transaction,
        Is_High_Risk_country,
        Daily_chargeback_avg_amt,
        six_month_avg_chbk_amt,
        six_month_chbk_freq,
):
    # Create a DataFrame with the input data
    input_data = {
        "Average Amount/transaction/day": [avg_amount_per_day],
        "Transaction_amount": [transaction_amount],
        "Is declined": [Is_declined],
        "Total Number of declines/day": [no_of_declines_per_day],
        "isForeignTransaction": [Is_Foreign_transaction],
        "isHighRiskCountry": [Is_High_Risk_country],
        "Daily_chargeback_avg_amt": [Daily_chargeback_avg_amt],
        "6_month_avg_chbk_amt": [six_month_avg_chbk_amt],
        "6-month_chbk_freq": [six_month_chbk_freq],
    }

    return pd.DataFrame(input_data)


def get_prediction(
        avg_amount_per_day,
        transaction_amount,
        Is_declined,
        no_of_declines_per_day,
        Is_Foreign_transaction,
        Is_High_Risk_country,
        Daily_chargeback_avg_amt,
        six_month_avg_chbk_amt,
        six_month_chbk_freq,
):

    # Convert "no" to 0 and "yes" to 1 for the relevant fields
    Is_declined = 0 if Is_declined.lower() == "no" else 1
    Is_Foreign_transaction = 0 if Is_Foreign_transaction.lower() == "no" else 1
    Is_High_Risk_country = 0 if Is_High_Risk_country.lower() == "no" else 1

    # Prepare the input data
    input_df = prepare_input_data(
        avg_amount_per_day,
        transaction_amount,
        Is_declined,
        no_of_declines_per_day,
        Is_Foreign_transaction,
        Is_High_Risk_country,
        Daily_chargeback_avg_amt,
        six_month_avg_chbk_amt,
        six_month_chbk_freq,
    )
    # print(input_df.values)
    # Load the model
    svm_model = load_model("models/credit_card_fraud/saved models/transaction_rf_model.pkl")

    # Predict using Random Forest
    predicted_value = svm_model.predict(input_df)

    # Return "Fraud" if fraud (1), else "Not a Fraud"
    return "Fraud" if predicted_value[0] == 1 else "Not a Fraud"

def model_details():
	"""Returns model evaluation details."""
	return get_evaluator()
