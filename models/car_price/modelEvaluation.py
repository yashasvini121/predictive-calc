
# modelEvaluation.py
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
    print(f'R² Score: {r2}')
    return predictions

def plot_predictions(y_test, predictions, model_name):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=predictions, alpha=0.6)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r')  # Diagonal line
    plt.title(f'{model_name} Predictions vs Actual Selling Prices')
    plt.xlabel('Actual Selling Prices')
    plt.ylabel('Predicted Selling Prices')
    plt.xlim(y_test.min() - 1000, y_test.max() + 1000)
    plt.ylim(y_test.min() - 1000, y_test.max() + 1000)
    plt.grid()
    plt.show()

def plot_feature_importance(model, feature_names):
    importance = model.coef_ if hasattr(model, 'coef_') else None
    if importance is not None:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=importance, y=feature_names)
        plt.title('Feature Importance')
        plt.xlabel('Coefficient Value')
        plt.ylabel('Features')
        plt.show()
