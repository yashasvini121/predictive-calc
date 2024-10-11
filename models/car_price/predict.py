# predict.py
from model import load_and_preprocess_data, train_linear_regression, train_lasso_regression
from modelEvaluation import evaluate_model, plot_predictions, plot_feature_importance

def main():
    # Path to the CSV file
    file_path = 'car_data.csv'  # Ensure this CSV file is in the same directory

    # Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data(file_path)
    
    # Train models
    lr_model = train_linear_regression(X_train, y_train)
    lasso_model = train_lasso_regression(X_train, y_train)

    # Evaluate models
    print("Evaluating Linear Regression:")
    lr_predictions = evaluate_model(lr_model, X_test, y_test)
    plot_predictions(y_test, lr_predictions, "Linear Regression")
    
    print("\nEvaluating Lasso Regression:")
    lasso_predictions = evaluate_model(lasso_model, X_test, y_test)
    plot_predictions(y_test, lasso_predictions, "Lasso Regression")

    # Plot feature importance for Lasso Regression
    plot_feature_importance(lasso_model, X_train.columns)

if __name__ == "__main__":
    main()
