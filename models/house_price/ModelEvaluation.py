import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error


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

		return metrics, prediction_plot, error_plot

	def get_metrics(self):
		"""Return a dictionary of evaluation metrics for easy integration."""
		pred_train = self.model.predict(self.train_X)
		pred_test = self.model.predict(self.test_X)

		metrics = {
			"Train_R2": r2_score(self.train_Y, pred_train),
			"Test_R2": r2_score(self.test_Y, pred_test),
			"Train_RSS": np.sum(np.square(self.train_Y - pred_train)),
			"Test_RSS": np.sum(np.square(self.test_Y - pred_test)),
			"Train_MSE": mean_squared_error(self.train_Y, pred_train),
			"Test_MSE": mean_squared_error(self.test_Y, pred_test),
			"Train_RMSE": np.sqrt(mean_squared_error(self.train_Y, pred_train)),
			"Test_RMSE": np.sqrt(mean_squared_error(self.test_Y, pred_test)),
		}
		return metrics

	def plot_predictions(self, pred_train):
		plt.figure(figsize=(15, 6))
		plt.scatter(
			self.train_X[self.random_column], self.train_Y, label="Actual", alpha=0.6
		)
		plt.scatter(
			self.train_X[self.random_column], pred_train, label="Prediction", alpha=0.6
		)
		plt.title("Actual vs Prediction")
		plt.xlabel(self.random_column)
		plt.ylabel("Price")
		plt.legend()
		plt.grid()
		plt.tight_layout()
		plt.show()  # Show the plot when generating
		return plt

	def update_evaluation_matrix(self, pred_train, pred_test):
		self.evaluation_matrix.loc[0] = [
			r2_score(self.train_Y, pred_train),
			r2_score(self.test_Y, pred_test),
			np.sum(np.square(self.train_Y - pred_train)),
			np.sum(np.square(self.test_Y - pred_test)),
			mean_squared_error(self.train_Y, pred_train),
			mean_squared_error(self.test_Y, pred_test),
			np.sqrt(mean_squared_error(self.train_Y, pred_train)),
			np.sqrt(mean_squared_error(self.test_Y, pred_test)),
		]

	def plot_error_terms(self, pred_train):
		fig, axes = plt.subplots(1, 2, figsize=(15, 6))

		# Plotting error distribution
		sns.histplot(self.train_Y - pred_train, bins=30, kde=True, ax=axes[0])
		axes[0].set_title("Error Terms Distribution")
		axes[0].set_xlabel("Errors")

		# Plotting actual vs predicted
		axes[1].scatter(self.train_Y, pred_train, alpha=0.6)
		axes[1].plot(
			[self.train_Y.min(), self.train_Y.max()],
			[self.train_Y.min(), self.train_Y.max()],
			"r--",
		)
		axes[1].set_title("Actual vs Predicted Prices")
		axes[1].set_xlabel("Actual Price")
		axes[1].set_ylabel("Predicted Price")

		plt.tight_layout()
		plt.show()  # Show the plots when generating
		return plt

	def plot_performance_graph(self):
		metrics = self.get_metrics()
		performance_data = {
			"Metric": ["Train RMSE", "Test RMSE"],
			"Value": [metrics["Train_RMSE"], metrics["Test_RMSE"]],
		}
		performance_df = pd.DataFrame(performance_data)

		plt.figure(figsize=(6, 4))
		sns.barplot(x="Metric", y="Value", data=performance_df)
		plt.title("Model Performance Comparison")
		plt.ylabel("RMSE")
		plt.tight_layout()
		plt.show()  # Show the plot when generating
		return plt
