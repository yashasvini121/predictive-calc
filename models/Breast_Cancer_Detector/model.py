import pickle
import numpy as np

Loaded_model = pickle.load(open("saved models/model_Breast_cancer.pkl", 'rb'))

def cancer_type_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = Loaded_model.predict(input_data_reshaped)[0]
    
    return prediction