## Breast Cancer Prediction using Machine Learning

**Overview**

This repository contains a machine learning model that predicts whether a breast cancer is malignant or benign based on various features. The model is trained on a dataset of breast cancer samples and uses a Ridge Classifier algorithm to make predictions.

**Dataset**

The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) Dataset, which is a publicly available dataset that contains 569 samples of breast cancer tissue, each described by 30 features.

**Features**

The features used in this project are:

* radius_mean
* texture_mean
* perimeter_mean
* area_mean
* smoothness_mean
* compactness_mean
* concavity_mean
* concave points_mean
* symmetry_mean
* fractal_dimension_mean
* radius_se
* texture_se
* perimeter_se
* area_se
* smoothness_se
* compactness_se
* concavity_se
* concave points_se
* symmetry_se
* fractal_dimension_se
* radius_worst
* texture_worst
* perimeter_worst
* area_worst
* smoothness_worst
* compactness_worst
* concavity_worst
* concave points_worst
* symmetry_worst
* fractal_dimension_worst

**Model**

The model used in this project is a Ridge Classifier, which is a type of linear classifier that uses L2 regularization to prevent overfitting.

**Performance**

The model achieves an accuracy of 96.5% on the test set, with a precision of 95.1% and a recall of 97.9%.

**Usage**

To use this model, simply clone this repository and run the `predict.py` script with the input data as a command-line argument. The input data should be a CSV file containing the features listed above.

**Requirements**

* Python 3.8+
* scikit-learn 1.0+
* pandas 1.3+
* numpy 1.20+

**Acknowledgments**

This project was inspired by the Breast Cancer Wisconsin (Diagnostic) Dataset, which is a publicly available dataset that contains 569 samples of breast cancer tissue, each described by 30 features.
