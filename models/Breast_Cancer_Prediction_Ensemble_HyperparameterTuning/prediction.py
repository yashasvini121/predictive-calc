from model import cancer_type_prediction

def get_prediction(input_data):
    radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst = input_data
    
    prediction = cancer_type_prediction(input_data)

    if prediction == 0:
        return "The Breast cancer is Malignant"
    else:
        return "The Breast Cancer is Benign"
