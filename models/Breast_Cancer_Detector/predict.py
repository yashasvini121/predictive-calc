# models/breast_cancer/model.py

import pickle
import numpy as np

Loaded_model = pickle.load(open("D:\DS_March\Projects\Breast_cancer_model.pkl", 'rb'))

def breast_cancer_prediction(radius_mean, texture_mean, perimeter_mean, area_mean, 
                             perimeter_se, area_se, radius_worst, texture_worst, 
                             perimeter_worst, area_worst, concavity_worst):
    input_data = np.asarray([radius_mean, texture_mean, perimeter_mean, area_mean, 
                             perimeter_se, area_se, radius_worst, texture_worst, 
                             perimeter_worst, area_worst, concavity_worst])
    input_data_reshaped = input_data.reshape(1,-1)
    prediction = Loaded_model.predict(input_data_reshaped)
    return prediction