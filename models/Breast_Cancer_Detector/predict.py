from models.Breast_Cancer_Detector.model import Loaded_model, cancer_type_prediction
import streamlit as st

def predict_cancer_type(input_data):

    expected_length = 30 
    if len(input_data) != expected_length:
        raise ValueError(f"Expected {expected_length} input features, but got {len(input_data)}.")
    
    prediction = cancer_type_prediction(input_data)
    return prediction

def test_prediction():
    st.title("Breast Cancer Type Prediction")

    mean_radius = st.number_input("Enter mean radius:", format="%.2f")
    mean_texture = st.number_input("Enter mean texture:", format="%.2f")
    mean_perimeter = st.number_input("Enter mean perimeter:", format="%.2f")
    mean_area = st.number_input("Enter mean area:", format="%.2f")
    mean_smoothness = st.number_input("Enter mean smoothness:", format="%.2f")
    mean_compactness = st.number_input("Enter mean compactness:", format="%.2f")
    mean_concavity = st.number_input("Enter mean concavity:", format="%.2f")
    mean_concave_points = st.number_input("Enter mean concave points:", format="%.2f")
    mean_symmetry = st.number_input("Enter mean symmetry:", format="%.2f")
    mean_fractal_dimension = st.number_input("Enter mean fractal dimension:", format="%.2f")
    radius_error = st.number_input("Enter radius error:", format="%.2f")
    texture_error = st.number_input("Enter texture error:", format="%.2f")
    perimeter_error = st.number_input("Enter perimeter error:", format="%.2f")
    area_error = st.number_input("Enter area error:", format="%.2f")
    smoothness_error = st.number_input("Enter smoothness error:", format="%.2f")
    compactness_error = st.number_input("Enter compactness error:", format="%.2f")
    concavity_error = st.number_input("Enter concavity error:", format="%.2f")
    concave_points_error = st.number_input("Enter concave points error:", format="%.2f")
    symmetry_error = st.number_input("Enter symmetry error:", format="%.2f")
    fractal_dimension_error = st.number_input("Enter fractal dimension error:", format="%.2f")
    worst_radius = st.number_input("Enter worst radius:", format="%.2f")
    worst_texture = st.number_input("Enter worst texture:", format="%.2f")
    worst_perimeter = st.number_input("Enter worst perimeter:", format="%.2f")
    worst_area = st.number_input("Enter worst area:", format="%.2f")
    worst_smoothness = st.number_input("Enter worst smoothness:", format="%.2f")
    worst_compactness = st.number_input("Enter worst compactness:", format="%.2f")
    worst_concavity = st.number_input("Enter worst concavity:", format="%.2f")
    worst_concave_points = st.number_input("Enter worst concave points:", format="%.2f")
    worst_symmetry = st.number_input("Enter worst symmetry:", format="%.2f")
    worst_fractal_dimension = st.number_input("Enter worst fractal dimension:", format="%.2f")

    input_data = [
        mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, 
        mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, 
        mean_fractal_dimension, radius_error, texture_error, perimeter_error, 
        area_error, smoothness_error, compactness_error, concavity_error, 
        concave_points_error, symmetry_error, fractal_dimension_error, 
        worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, 
        worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, 
        worst_fractal_dimension
    ]

    prediction = predict_cancer_type(input_data)

    st.write("Predicted cancer type:", prediction)
