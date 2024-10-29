import numpy as np 
import pandas as pd 
import pickle
import os
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
# Load the data
df = pd.read_csv('50_Startups.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Preprocessing - Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

# Splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Training the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print predictions alongside actual values
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)), axis=1))

model_path = os.path.abspath("model.pkl")
scaler_path = os.path.abspath("scaler.pkl")

# Save the model and preprocessing objects
with open(model_path, 'wb') as model_file:
    pickle.dump(model, model_file)

with open(scaler_path, 'wb') as scaler_file:
    pickle.dump(ct, scaler_file)

print("Model and preprocessing objects saved successfully!")

def save_evaluation_to_pickle(train_X, train_Y, test_X, test_Y, output_file="evaluation_results.pkl"):
    # Calculate R^2 score
    train_r2 = r2_score(train_Y, model.predict(train_X))
    test_r2 = r2_score(test_Y, y_pred)

    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(test_Y, y_pred, alpha=0.6, color='blue', label='Predicted')
    ax.plot([test_Y.min(), test_Y.max()], [test_Y.min(), test_Y.max()], 'r--', label='Perfect Prediction')
    ax.set_xlabel("Actual")
    ax.set_ylabel("Predicted")
    ax.set_title("Actual vs Predicted Values (Test Set)")
    ax.legend()
    ax.grid(True)

    # Save the plot as a PNG file
    plot_file = "actual_vs_predicted.png"
    fig.savefig(plot_file)

    # Package results
    results = {
        "Train_R2": train_r2,
        "Test_R2": test_r2,
        "plot_file": plot_file  # Save the plot file path
    }

    # Save results to a pickle file
    with open(output_file, "wb") as f:
        pickle.dump(results, f)

    print(f"Evaluation and plot data saved to {output_file}")
    print(f"Plot saved as {plot_file}")
# Run this function once to generate the evaluation file
save_evaluation_to_pickle(X_train, y_train, X_test, y_test)