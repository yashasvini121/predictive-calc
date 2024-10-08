from model import Loaded_model, cancer_type_prediction

def main():
    mean_radius = float(input("Enter mean radius: "))
    mean_texture = float(input("Enter mean texture: "))
    mean_perimeter = float(input("Enter mean perimeter: "))
    mean_area = float(input("Enter mean area: "))
    mean_smoothness = float(input("Enter mean smoothness: "))
    mean_compactness = float(input("Enter mean compactness: "))
    mean_concavity = float(input("Enter mean concavity: "))
    mean_concave_points = float(input("Enter mean concave points: "))
    mean_symmetry = float(input("Enter mean symmetry: "))
    mean_fractal_dimension = float(input("Enter mean fractal dimension: "))
    radius_error = float(input("Enter radius error: "))
    texture_error = float(input("Enter texture error: "))
    perimeter_error = float(input("Enter perimeter error: "))
    area_error = float(input("Enter area error: "))
    smoothness_error = float(input("Enter smoothness error: "))
    compactness_error = float(input("Enter compactness error: "))
    concavity_error = float(input("Enter concavity error: "))
    concave_points_error = float(input("Enter concave points error: "))
    symmetry_error = float(input("Enter symmetry error: "))
    fractal_dimension_error = float(input("Enter fractal dimension error: "))
    worst_radius = float(input("Enter worst radius: "))
    worst_texture = float(input("Enter worst texture: "))
    worst_perimeter = float(input("Enter worst perimeter: "))
    worst_area = float(input("Enter worst area: "))
    worst_smoothness = float(input("Enter worst smoothness: "))
    worst_compactness = float(input("Enter worst compactness: "))
    worst_concavity = float(input("Enter worst concavity: "))
    worst_concave_points = float(input("Enter worst concave points: "))
    worst_symmetry = float(input("Enter worst symmetry: "))
    worst_fractal_dimension = float(input("Enter worst fractal dimension: "))

    input_data = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]

    prediction = cancer_type_prediction(input_data)

    print("Predicted cancer type:", prediction)

if __name__ == "__main__":
    main()