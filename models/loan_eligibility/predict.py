import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

# Simulate some data (Loan Amount, Credit Score, Income)
np.random.seed(42)
data_size = 1000

income = np.random.randint(0, 150001, size=data_size)  # Income between 0 and ₹1.5 Lakhs
loan_amount = np.random.randint(5000, 50000, size=data_size)  # Loan amount between ₹5k and ₹50k
credit_score = np.random.randint(300, 850, size=data_size)  # Credit score between 300 and 850

# Derived feature: Loan-to-Income Ratio
loan_to_income_ratio = loan_amount / (income + 1)  # Adding 1 to avoid division by zero

# Function to determine eligibility 
def is_eligible(income, loan_amount, credit_score):
    # Simple rule-based eligibility logic
    if income > 40000 and loan_amount < 0.3 * income and credit_score > 600:
        return 1  # Eligible
    else:
        return 0  # Not Eligible

eligibility = np.array([is_eligible(income[i], loan_amount[i], credit_score[i]) for i in range(data_size)])

# Create a DataFrame for training
df = pd.DataFrame({
    'Income': income,
    'Loan Amount': loan_amount,
    'Credit Score': credit_score,
    'Loan-to-Income Ratio': loan_to_income_ratio,
    'Eligibility': eligibility
})

#Features and target
X = df[['Income', 'Loan Amount', 'Credit Score', 'Loan-to-Income Ratio']]
y = df['Eligibility']

# Split the data into training and testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Training Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Create the Streamlit app
st.title("Loan Eligibility Predictor ")

# User inputs
income_input = st.number_input("Enter your Income (₹)", min_value=0, step=5000, format="%d")  # No upper cap on income

# Calculate 80% of income as the maximum loan amount
max_loan_amount = 0.8 * income_input if income_input > 0 else 5000

# Ensure that loan amount is at least 5000 and dynamically adjust the upper limit
loan_amount_input = st.number_input(f"Enter the Loan Amount you want (₹)", 
                                    min_value=5000, 
                                    max_value=int(max_loan_amount), 
                                    step=1000)

credit_score_input = st.number_input("Enter your Credit Score", min_value=300, max_value=850, step=10)

# Derived feature: Loan-to-Income Ratio
loan_to_income_ratio_input = loan_amount_input / (income_input + 1)  # Adding 1 to avoid division by zero

# Prediction button
if st.button("Check Eligibility"):
    # Predict eligibility based on user inputs
    new_data = np.array([[income_input, loan_amount_input, credit_score_input, loan_to_income_ratio_input]])
    prediction = model.predict(new_data)
    
    if prediction == 1:
        st.success("You are Eligible for the loan!")
    else:
        st.error("You are Not Eligible for the loan.")
