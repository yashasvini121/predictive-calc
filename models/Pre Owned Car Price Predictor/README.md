# Pre-Owned Car Price Predictor

## Overview
The **Pre-Owned Car Price Predictor** is a machine learning project aimed at predicting the prices of pre-owned cars based on various features such as make, model, year, mileage, and fuel type. This tool helps potential buyers and sellers get an accurate price estimation for used cars, enabling informed decision-making in the car resale market.

## Features
- **Comprehensive Dataset Analysis**: The project uses a dataset with essential car details, including make, model, year, mileage, fuel type, and price, for model training.
- **Model Performance Evaluation**: The model's performance is measured using Mean Absolute Error (MAE) and R-squared metrics to ensure accurate predictions.

## Technologies Used
- **Python**: The primary programming language used in the project.
- **Machine Learning**: Predictive modeling to estimate car prices based on user inputs.
- **Scikit-Learn**: Used for model building and evaluation.
- **Pandas and NumPy**: Data manipulation and preprocessing.
- **Matplotlib and Seaborn**: Data visualization for analyzing relationships and trends within the data.

## Skills Demonstrated
1. **Data Preprocessing**: Cleaning and transforming raw data for analysis and model training.
2. **Data Manipulation**: Extracting meaningful features and organizing data for the model.
3. **Data Visualization**: Using plots and charts to understand data distributions and correlations.
4. **Data Cleaning**: Handling missing values and removing outliers to improve model accuracy.
5. **Statistical Analysis**: Assessing relationships between features and the target variable.
6. **Machine Learning Modeling**: Building and evaluating predictive models.
7. **Problem Solving**: Developing a solution for price prediction in a real-world context.

## Data Sources
 
- **Data Preprocessing**: Extensive preprocessing was required to clean the data, handle missing values, and engineer features for analysis.

## Model Training and Evaluation
- The machine learning model was trained using a **Linear Regression** algorithm, achieving an accuracy of **86%** on the test set.
- **Model Pipeline**: A robust pipeline was built to automate preprocessing and model training steps, making the solution scalable.
- **Hyperparameter Tuning**: Parameters were optimized to enhance the model's accuracy and generalization.

## Getting Started

### Prerequisites
- Python 3.x
- Required packages listed in `requirements.txt`

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yashasvini121/predictive-calc
    ```
2. Navigate to the project directory:
    ```bash
    cd car-price-predictor
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure
- `LinearRegressionModel.pkl`: Serialized machine learning model.
- `Cleaned_Car_data.csv`: The cleaned dataset used for training.


## Acknowledgments

- **Libraries and Tools**: Python,  Scikit-Learn, Pandas, NumPy, Matplotlib, and Seaborn for their support in building this project.

