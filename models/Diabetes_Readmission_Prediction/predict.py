from models.Diabetes_Readmission_Prediction.model import DiabetesModel

model_path = 'models/Diabetes_Readmission_Prediction/saved_models/rf_model_selected.joblib'

def get_prediction(num_lab_procedures, num_medications, time_in_hospital, preceding_year_visits, age):
    model = DiabetesModel(model_path)  # Initialize the DiabetesModel object

    # Create the input_data dictionary from the keyword arguments
    input_data = {
        'num_lab_procedures': num_lab_procedures,
        'num_medications': num_medications,
        'time_in_hospital': time_in_hospital,
        'preceding_year_visits': preceding_year_visits,
        'age': age
    }

    return model.predict(input_data)  # Call the predict method with input data


