from models.Heat_Cool_Load_Predictor.model import cool_load_prediction

def get_prediction(relative_compactness, surface_area, wall_area, roof_area, overall_height, orientation, glazing_area, glazing_area_distribution):
    return cool_load_prediction(relative_compactness, surface_area, wall_area, roof_area, overall_height, orientation, glazing_area, glazing_area_distribution)
