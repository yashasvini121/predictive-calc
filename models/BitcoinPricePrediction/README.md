## Bitcoin Price Prediction using LSTM
This repository contains an implementation of a Long Short-Term Memory (LSTM) model for predicting Bitcoin prices using historical data. The model is built using Keras and TensorFlow. It predicts the closing price of Bitcoin by training on past data and evaluating its performance on a test set. The results are evaluated using common regression metrics such as R², RMSE, MAE, and others.

## **Dataset**
The dataset used in this project is historical Bitcoin price data downloaded from a public source. The file BTC-USD.csv contains columns such as Date, Open, High, Low, Close, Adj Close, and Volume. The prediction is based solely on the Close price of Bitcoin.

**Dataset Preprocessing:**
* Missing values are handled.
* The Date column is converted into datetime format and set as the index.
* The closing prices are normalized using MinMaxScaler for better model performance.
  
## Model Architecture
The implemented model is a multi-layer LSTM neural network that includes dropout layers to reduce overfitting. Here's an overview of the model:

**Input Layer:** Time series data reshaped to 3D for LSTM layers.
**LSTM Layers:** Two LSTM layers with 200 and 160 units, respectively, with return_sequences enabled in the first layer.
**Dropout:** Added after each LSTM layer to prevent overfitting.
**Dense Layers:** Two Dense layers; the final layer has 1 neuron for regression output (predicted closing price).

## Model Hyperparameters
**Batch Size:** 32
**Epochs:** 50
**Loss Function:** Mean Squared Error (MSE)
**Optimizer:** Adam
**Metrics:** Mean Absolute Percentage Error (MAPE)

## Evaluation Metrics
The model is evaluated using several regression metrics, including:

* **R² Score:** Measures the proportion of variance in the dependent variable that is predictable.
* **RMSE:** Root Mean Squared Error, used to measure the differences between predicted and observed values.
* **MSE:** Mean Squared Error, similar to RMSE but without square rooting.
* **MAE:** Mean Absolute Error, the average of the absolute errors between actual and predicted values.
* **MATE:** Median Absolute Error, a robust measure of error.
* **SMATE:** Scaled Mean Absolute Error, normalized version of MAE.

  A detailed comparison of the training and testing set metrics is included in the project.

