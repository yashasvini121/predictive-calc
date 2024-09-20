# Predictive Calc

## Overview
**Predictive Calc** is an open-source project that provides a flexible collection of machine learning models designed to predict a wide variety of outcomes. Built with **Python** and **Streamlit**, the project offers an intuitive web interface, enabling users to easily interact with the models. The primary goal of the project is to streamline the integration of machine learning models with custom forms, allowing users to build their own prediction calculators tailored to specific use cases.

## Current Status
The project is under active development with several machine learning models already implemented for various prediction tasks. The architecture is designed for dynamic configuration using JSON files, which map model parameters, inputs, and features. This design ensures new models can be seamlessly added or updated with minimal modification to the core codebase.

The project has been successfully tested in local environments, and current efforts are focused on enhancing integration, optimizing deployment, and improving scalability for production-ready applications.

## How to Contribute:
1. Review existing issues and contribute towards resolving them.
2. Or create new issues to discuss new ideas, suggest features, or report bugs.
3. Fork the repository and create a new branch for your contribution.
4. Implement your changes and submit a pull request with a clear description.
5. Futher details can be found in the [contributing.md](contributing.md) file.

## Setup Instructions
1. Fork or clone the repository.
2. Create a virtual environment and install the necessary dependencies:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   ```
2. Install the necessary dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the Streamlit application using:
   ```powershell
   streamlit run app.py
   ```
