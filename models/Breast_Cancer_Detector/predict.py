import pickle
import numpy as np

Loaded_model = pickle.load(open("D:\DS_March\Projects\Breast_cancer_model.pkl", 'rb'))

input_data = (14.13, 19.69, 99.44, 624.4, 10.114, 0.905, 15.71, 25.38, 110.6, 730.6, 0.268)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for one datapoint
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = Loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The Breast cancer is Malignant')

else:
  print('The Breast Cancer is Benign')

'''
Index(['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'perimeter_se', 'area_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'concavity_worst'],
      dtype='object')
'''
