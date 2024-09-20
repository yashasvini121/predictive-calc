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
			train_X.loc[:, train_X.nunique() >= 50].columns.values, 1, replace=False
		)[0]

	def evaluate(self):
		pred_train = self.model.predict(self.train_X)
		pred_test = self.model.predict(self.test_X)

		self.plot_predictions(pred_train)
		self.print_metrics(pred_train, pred_test)
		self.update_evaluation_matrix(pred_train, pred_test)
		self.plot_error_terms(pred_train)

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
		plt.figure(figsize=[15, 6])
		plt.subplot(2, 3, 1)
		plt.scatter(self.train_X[self.random_column], self.train_Y, label="Actual")
		plt.scatter(self.train_X[self.random_column], pred_train, label="Prediction")
		plt.legend()
		plt.title("Actual vs Prediction")
		plt.xlabel(self.random_column)
		plt.ylabel("Price")
		plt.show()

	def print_metrics(self, pred_train, pred_test):
		metrics = {
			"Training": {
				"R2": r2_score(self.train_Y, pred_train),
				"RSS": np.sum(np.square(self.train_Y - pred_train)),
				"MSE": mean_squared_error(self.train_Y, pred_train),
				"RMSE": np.sqrt(mean_squared_error(self.train_Y, pred_train)),
			},
			"Testing": {
				"R2": r2_score(self.test_Y, pred_test),
				"RSS": np.sum(np.square(self.test_Y - pred_test)),
				"MSE": mean_squared_error(self.test_Y, pred_test),
				"RMSE": np.sqrt(mean_squared_error(self.test_Y, pred_test)),
			},
		}

		for phase, values in metrics.items():
			print(f"\n{'-' * 20} {phase} Set Metrics {'-' * 20}")
			for metric, value in values.items():
				print(f"{metric} ---> {round(value, 20)}")

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
		print("\nEvaluation Matrix:\n", self.evaluation_matrix)

	def plot_error_terms(self, pred_train):
		plt.figure(figsize=[15, 4])

		plt.subplot(1, 2, 1)
		sns.histplot((self.train_Y - pred_train), bins=30, kde=True)
		plt.title("Error Terms")
		plt.xlabel("Errors")

		plt.subplot(1, 2, 2)
		plt.scatter(self.train_Y, pred_train)
		plt.plot(
			[self.train_Y.min(), self.train_Y.max()],
			[self.train_Y.min(), self.train_Y.max()],
			"r--",
		)
		plt.title("Actual vs Predicted")
		plt.xlabel("Actual Price")
		plt.ylabel("Predicted Price")
		plt.show()
