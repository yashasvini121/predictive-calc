import base64
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import plotly.express as px

# Load pre-trained models and scaler
model_file_path = '../saved_models/model.pkl'
scaler_file_path = '../saved_models/scaler.pkl'

with open(model_file_path, 'rb') as f:
    model = pickle.load(f)

with open(scaler_file_path, 'rb') as f:
    scaler = pickle.load(f)

# Load the dataset
data_file_path = "../cervical_cancer/data/kag_risk_factors_cervical_cancer.csv"
data = pd.read_csv(data_file_path)

# Replace '?' with NaN
data.replace('?', np.nan, inplace=True)

# Convert all columns to numeric
data = data.apply(pd.to_numeric, errors='coerce')

# Drop rows with missing target values
data.dropna(subset=['Dx'], inplace=True)

# Features (X) and Target (y)
X = data.drop(columns=['Dx'])
y = data['Dx']

# Impute missing values with the median
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)

# Scaling (assumes scaler is pre-fitted)
X_scaled = scaler.transform(X_imputed)

# Streamlit app setup
st.set_page_config(page_title="Cervical Cancer Prediction", page_icon="💉", layout="centered")

# App Title
st.markdown("<h1 style='text-align: center; color: #FF6347;'>Cervical Cancer Prediction</h1>", unsafe_allow_html=True)

# Load and display image
image_path = "../assets/img1.jpg"  # Update the path as per your project
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/jpg;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" width="400" />
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar for inputs
st.sidebar.markdown("## Input Features")
st.sidebar.markdown("Provide information to predict cervical cancer risk.")

def user_input_features():
    binary_columns = [
        'Smokes', 'Hormonal Contraceptives', 'IUD', 'STDs', 'STDs (number)',
        'STDs:condylomatosis', 'STDs:cervical condylomatosis', 'STDs:vaginal condylomatosis',
        'STDs:vulvo-perineal condylomatosis', 'STDs:syphilis', 'STDs:pelvic inflammatory disease',
        'STDs:genital herpes', 'STDs:molluscum contagiosum', 'STDs:AIDS', 'STDs:HIV',
        'STDs: Number of diagnosis', 'Dx:CIN', 'Dx:HPV', 'Dx:Cancer', 'Hinselmann', 'Schiller',
        'Citology', 'Biopsy'
    ]
    
    inputs = {}
    
    # Binary columns input
    for col in binary_columns:
        inputs[col] = st.sidebar.selectbox(f"{col}", options=[0, 1], index=0)
    
    # Other columns
    other_columns = [col for col in X.columns if col not in binary_columns]
    for col in other_columns:
        inputs[col] = st.sidebar.number_input(f"{col}", min_value=0, value=0)

    input_data = pd.DataFrame([inputs])
    input_data = input_data[X.columns]  # Ensure column order matches the dataset
    return input_data

# Get user inputs
input_data = user_input_features()

# Impute and scale user input data
input_data_imputed = imputer.transform(input_data)
input_data_scaled = scaler.transform(input_data_imputed)

# Display user inputs
st.markdown("### User Input Features")
st.write(input_data)

st.markdown("---")

# Prediction button
if st.button("Predict"):
    st.markdown("### Predictions")
    prediction = model.predict(input_data_scaled)[0]
    prediction_proba = model.predict_proba(input_data_scaled)[0][1] if hasattr(model, "predict_proba") else None

    prediction_text = 'Cancer Detected' if prediction == 1 else 'No Cancer Detected'
    
    if prediction == 1:
        st.success(f"{prediction_text}")
    else:
        st.info(f"{prediction_text}")
    
    if prediction_proba is not None:
        st.markdown(f"Probability of Cancer: **{prediction_proba:.2f}**")

    st.markdown("---")

# Evaluate model on test data (Optional)
st.markdown("### Model Accuracy on Test Set")
y_pred = model.predict(X_scaled)
accuracy = accuracy_score(y, y_pred)

# Plot accuracy
fig = px.bar(
    x=["Model"], 
    y=[accuracy], 
    labels={'x': 'Model', 'y': 'Accuracy'}, 
    title='Model Accuracy',
    text=[f'{accuracy:.2f}']
)
fig.update_traces(marker_color='#FFA07A', textposition='auto')
st.plotly_chart(fig)

# Footer
st.markdown("<hr><p style='text-align: center; color: grey;'>Developed by Spandana</p>", unsafe_allow_html=True)
