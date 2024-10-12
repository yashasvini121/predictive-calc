## How to Integrate Your Model

To integrate a new machine learning model into **Predictive Calc**, follow these steps:

### 1. Create Your Model Directory
Navigate to the `models/` directory and create a new folder for your model. The folder should be named based on the problem your model addresses (e.g., `models/loan_eligibility/`).

Inside your folder, you’ll need the following structure:
```
models/
├── loan_approval/
│   ├── data/                         # Folder for storing the dataset used for training
│   ├── notebooks/                    # Jupyter notebooks for training and experimentation
│   ├── saved_models/                 # Folder for saving the trained model and any scalers
│   ├── model.py                      # Script to define and train your model
│   ├── predict.py                    # Script to load the trained model and make predictions
│   ├── modelEvaluation.py            # (Optional) Script for model evaluation and testing
```

### 2. Train Your Model
Train your model in a Jupyter notebook and save the final trained model as a pickle file (`model.pkl`) inside the `saved_models/` folder. If your model requires preprocessing steps like scaling or encoding, save these objects as well (e.g., `scaler.pkl`).

### 3. Define the Prediction Logic
In `predict.py`, load your saved model and write the logic for making predictions. This file should accept input data (coming from the web form) and return the prediction result.

### 4. Configure the Input Form
In the `form_configs/` folder, create a new JSON configuration file (e.g., `loan_eligibility.json`). This file defines the fields that will appear in the input form and maps them to the prediction model’s expected input parameters.

### 5. Configure the Page Settings
In the `pages/pages.json` file, add an entry for your new model. This configuration file manages the settings for all pages in the application, including titles, icons, model paths, and tab configurations.

### 6. Add a Streamlit Page
- In the `pages/` directory, create a new Python file for the web interface (e.g., `loan_approval_calculator.py`). This file will call the `page_handler.py` script to render the form and display the prediction results.
- The page name on the sidebar will be same as the file name.

### 7. Update the Main App
In `app.py`, update the list of available pages