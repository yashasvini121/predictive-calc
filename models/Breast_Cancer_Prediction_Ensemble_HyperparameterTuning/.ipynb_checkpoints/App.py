from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)


with open('model.pkl', 'rb') as f:
    ridge = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = data['input_data']
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = ridge.predict(input_data_reshaped)
    if (prediction[0] == 0):
        result = 'Malignant'
    else:
        result = 'Benign'

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
