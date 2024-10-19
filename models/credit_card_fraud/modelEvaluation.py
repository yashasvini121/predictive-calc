import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix


class ModelEvaluation:
    def __init__(self, model, train_X, train_Y, test_X, test_Y):
        self.model = model
        self.train_X = train_X
        self.train_Y = train_Y
        self.test_X = test_X
        self.test_Y = test_Y
        self.evaluation_matrix = pd.DataFrame(
            np.zeros([1, 8]),
            columns=[
                "Train-R2",
                "Test-R2",
                "Train-RSS",
                "Test-RSS",
                "Train-MSE",
                "Test-MSE",
                "Train-RMSE",
                "Test-RMSE",
            ],
        )
        self.random_column = np.random.choice(
            train_X.columns[train_X.nunique() >= 50], 1, replace=False
        )[0]

    def evaluate(self):
        pred_train = self.model.predict(self.train_X)
        pred_test = self.model.predict(self.test_X)

        self.update_evaluation_matrix(pred_train, pred_test)
        metrics = self.get_metrics()
        prediction_plot = self.plot_predictions(pred_train)
        error_plot = self.plot_error_terms(pred_train)

        # adding performance graph of the model
        performance_plot = self.plot_performance_graph()

        return metrics, prediction_plot, error_plot, performance_plot

    def get_metrics(self):
        """Return a dictionary of evaluation metrics for easy integration."""
        pred_train = self.model.predict(self.train_X)
        pred_test = self.model.predict(self.test_X)

        metrics = {
            "Train_R2": accuracy_score(self.train_Y, pred_train),
            "Test_R2": accuracy_score(self.test_Y, pred_test),
            "Train_RSS": np.sum(np.square(self.train_Y - pred_train)),
            "Test_RSS": np.sum(np.square(self.test_Y - pred_test))
        }
        return metrics

    def plot_predictions(self, pred_train):
        # Predict on test data
        pred_test = self.model.predict(self.test_X)

        # Calculate confusion matrix
        cm = confusion_matrix(self.test_Y, pred_test)

        # Plot confusion matrix
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)

        ax.set_title("Confusion Matrix")
        ax.set_xlabel("Predicted Labels")
        ax.set_ylabel("True Labels")

        plt.tight_layout()
        return fig

    def update_evaluation_matrix(self, pred_train, pred_test):
        return

    # making a separate function for plotting error terms
    def plot_error_terms(self, pred_train):
        fig, axes = plt.subplots(figsize=(15, 6))

        # Plotting error distribution
        sns.histplot(self.train_Y - pred_train, bins=30, kde=True, ax=axes)
        axes.set_title("Error Terms Distribution")
        axes.set_xlabel("Errors")

        plt.tight_layout()
        return fig  # returning figure the is created here

    def plot_performance_graph(self):
        # Predict on test data
        pred_test = self.model.predict(self.test_X)

        # Calculate confusion matrix
        cm = confusion_matrix(self.test_Y, pred_test)

        # Plot confusion matrix
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)

        ax.set_title("Confusion Matrix")
        ax.set_xlabel("Predicted Labels")
        ax.set_ylabel("True Labels")

        plt.tight_layout()
        return fig
