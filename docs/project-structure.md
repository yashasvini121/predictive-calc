# Project Structure

The directory layout of **Predictive Calc** is organized in a way that separates concerns between model development, frontend interaction, and configuration management. Below is a breakdown of the key folders and files:

```
predictive-calc/
├── app.py                           # Main entry point for the Streamlit web app
├── docs/                            # Documentation files
│   ├── project-structure.md         	# Directory layout of the repository
│   ├── tutorial.md                  	# Steps to integrate a new machine learning model into the repository 
├── form_configs/                    # Configuration files for the forms
│   ├── house_price.json             	# JSON configuration for house price model form input fields
│   ├── loan_eligibility.json        	# JSON configuration for loan eligibility model form input fields
│   ├── ...
├── models/                          # Folder containing machine learning models
│   ├── house_price/                 	# Example model directory (for house price prediction)
│   │   ├── data/                    	  # Datasets used by the models
│   │   ├── notebooks/               		# Jupyter notebooks for dataset exploration and model training
│   │   │   ├── house_price.ipynb 
│   │   ├── saved_models/            		# Serialized (pickled) model files and scalers
│   │   │   ├── model.pkl            			# Trained model for predictions
│   │   │   ├── scaler.pkl           			# Scaler for data normalization
│   │   ├── model.py                 	# Code to define and train the model
│   │   ├── predict.py               	# Code to make predictions using the trained model. Contain get_prediction() function
│   ├── modelEvaluation.py           # Model evaluation class generates plots and metrics
│   ├── ...
├── pages/                           # Streamlit pages representing different calculators
│   ├── pages.json                   	# Configuration file for managing page details and settings
│   ├── House_Price_Estimator.py    
│   ├── Loan_Eligibility_Estimator.py
│   ├── ...
├── assets/
│   ├── images/                      # Image assets used in the Streamlit app                  
│   │   ├── machine-learning.png
│   │   ├── machine-learning.gif
│   │   ├── ...
├── form_handler.py                  # Class to handle dynamic form generation based on JSON configs
├── page_handler.py                  # Class to manage the page rendering logic and handles model predictions
├── requirements.txt                 # List of Python dependencies required for the Streamlit App
├── dev-requirements.txt             # Development dependencies, including Jupyter and tools for local use, excluding those needed for production Streamlit
├── packages.txt                     # List of Ubuntu packages required for Streamlit App
├── Dockerfile                       # Instructions for building a Docker Image
├── docker-compose.yml               # To set up a docker container for streamlit
├── docker-compose.debug.yml         # To debug inside the docker container using Debugpy
├── readme.md                        # Overview of the project and setup instructions
```

### Key Components

#### 1. `app.py`
This is the entry point for the **Streamlit** application. It initializes the app and renders the home page, and loads the model calculators having their pages in the `pages/` directory.

#### 2. `page_handler.py`
The page_handler.py file manages the rendering of pages in the Predictive Calc application by reading configurations from the pages.json file. It dynamically loads page titles, icons, and model paths, ensuring a smooth user experience. The class integrates model prediction logic and utilizes the `FormHandler` to generate dynamic forms based on the specified configurations. It also manages multiple tabs, enhancing functionality and allowing for easy updates or additions of new models while maintaining a cohesive interface.

#### 3. `form_handler.py`
This script dynamically generates the input forms based on the JSON configuration files. It maps user inputs to the model’s expected parameters and passes the data to the prediction logic.

#### 4. `models/`
Each model gets its own folder within the `models/` directory, which contains all necessary files for that particular model. This includes:
- **notebooks/**: Jupyter notebooks for model training and experimentation.
- **model.py**: Code defining and training the finally chosen machine learning model.
- **predict.py**: Code to load the trained model and make predictions based on user input.
- **saved_models/**: Directory where the trained model (`model.pkl`) and any preprocessing objects like scalers (`scaler.pkl`) are stored.
- **data/**: Raw datasets used for training the model.
- **modelEvaluation.py**: Scripts for model evaluation and reporting.

#### 5. `pages/`
Each model has a corresponding Streamlit page in the `pages/` folder. This page handles the frontend logic, rendering the forms for user input and displaying the prediction results. For example, the `house_price_calculator.py` page contains the interface for the house price prediction model.

#### 6. `pages/pages.json`
This file manages the configuration for all pages in the application, defining attributes such as titles, icons, model paths, and tab configurations for each calculator. This centralizes the configuration for easier updates and management of multiple pages.

#### 7. `form_configs/`
The `form_configs/` folder contains JSON configuration files that define the input fields required by each model. These JSON files dictate how the forms are dynamically generated by `form_handler.py`. For example, the `house_price.json` file specifies the input fields (e.g., square footage, number of bedrooms, etc.) needed for the house price prediction model.

#### 8. `docs/`
Contains the project's documentation. This is where you can find information about how the system is structured and how to contribute to the project, more specifically the `tutorial.md` and `project-stuctures.md` files.

#### 9. `requirements.txt`, `dev-requirements.txt`, `packages.txt`
- `requirements.txt` contains the Python dependencies required to run the Streamlit application.
- `dev-requirements.txt` includes additional dependencies for development purposes, such as Jupyter notebooks and other tools.
- `packages.txt` lists the Ubuntu packages required for the Streamlit application to run correctly.

#### 10. `Dockerfile`, `docker-compose.yml`, `docker-compose.debug.yml`
- `Dockerfile` contains the instructions for building a Docker image that can run the Streamlit application.
- `docker-compose.yml` sets up a Docker container for the Streamlit application.
- `docker-compose.debug.yml` allows debugging inside the Docker container using Debugpy.

#### 11. `assets/`
This folder contains all the assets used in the main project.
