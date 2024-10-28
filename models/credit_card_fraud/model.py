# importing libraries
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd
import warnings
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
import pickle
from models.credit_card_fraud.modelEvaluation import ModelEvaluation
warnings.filterwarnings("ignore")


# reading dataset
data = pd.read_csv("models/credit_card_fraud/data/creditcardcsvpresent.csv")
df = data.copy(deep=True)

# df.info()

# remove transaction_date all values are null
# and also remove merchant id
df = df.drop(columns=['Merchant_id', 'Transaction date'], axis=1)


# encoding for qualitative variables
code = {
    "N": 0,
    "Y": 1 }

for obj in df.select_dtypes("object"):
    df[obj] = df[obj].map(code)

# Target and Feature Identification
target = "isFradulent"
features = [col for col in df.columns if col != target]

X = df[features]  # Create a DataFrame for the features
y = df[target]   # Create a Series for the target


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM Classifier
svm_model = SVC(kernel='rbf', class_weight='balanced', random_state=42)  # RBF kernel (default) is good for non-linear problems
svm_model.fit(X_train, y_train)

# Make predictions
y_pred = svm_model.predict(X_test)

# Function to prepare input data into a DataFrame
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
    # Predict using Random Forest
    predicted_value = svm_model.predict(input_df)

    # Return "Fraud" if fraud (1), else "Not a Fraud"
    return "Fraud" if predicted_value[0] == 1 else "Not a Fraud"


# Function to save the model
def save_model():
    # Save the Random Forest model
    model_filename = 'creditCardFraud_svc_model.pkl'
    with open(model_filename, 'wb') as file:
        pickle.dump(svm_model, file)

# # Function to evaluate accuracy
def get_evaluator():
	evaluator = ModelEvaluation(svm_model, X_train, y_train, X_test, y_test)	
	return evaluator

# save_model()
