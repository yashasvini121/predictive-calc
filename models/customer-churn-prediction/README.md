# Customer Churn Prediction with Random Forest

## 📝 Project Overview
This project aims to predict customer churn in a subscription-based service using a Random Forest Classifier. Customer churn prediction is critical for businesses like telecom, where retaining customers is essential to sustain revenue. By identifying customers likely to churn, companies can take proactive retention measures.

## 📊 Dataset
The project uses the **Telco Customer Churn Dataset**, which contains information on customer demographics, service usage, and account details.

### Dataset Columns
- **Demographics**: Gender, senior citizen status, partner status, etc.
- **Account Details**: Contract type, payment method, tenure, etc.
- **Service Usage**: Internet service, additional services like streaming, etc.
- **Target Variable**: `Churn` (Yes or No)

## 🧠 Model Description
The Random Forest Classifier is chosen for its ability to handle a mixture of feature types and evaluate feature importance. This interpretable, efficient model is suited for binary classification tasks like churn prediction.

## 🔍 Project Steps
1. **Data Loading and Preprocessing**: 
   - Remove irrelevant columns (e.g., `customerID`).
   - Encode categorical features and target variable.
   - Scale numerical features.

2. **Train-Test Split**:
   - Split the dataset into training and testing sets.

3. **Model Training**:
   - Use the Random Forest Classifier with 100 trees and fit it to the training data.

4. **Evaluation**:
   - Measure accuracy, precision, recall, and F1 score to assess model performance.
   - Generate a classification report and display feature importance.

5. **Feature Importance Analysis**:
   - Identify key factors influencing customer churn, which can aid in designing retention strategies.

## 📈 Results
- The model aims for an accuracy of 80-85%, with precision, recall, and F1-score providing further insights into its performance.
- Feature importance analysis helps identify significant attributes, like `Contract Type`, `Tenure`, and `Monthly Charges`, which are closely linked to churn.

## 🚀 Running the Project
1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies**:
   ```bash
   pip install pandas scikit-learn
3. Run the script:
   ```bash
   python churn_prediction.py

## 📄 Future Improvements
- Experiment with other models (e.g., Gradient Boosting, XGBoost) for potential accuracy gains.
- Tune hyperparameters to enhance model performance.
- Apply cross-validation for a more robust evaluation. 
