from joblib import load

heat_model = load('models/Heat_Cool_Load_Predictor/saved_models/heat_model.pkl')
cool_model = load('models/Heat_Cool_Load_Predictor/saved_models/cool_model.pkl')

def heat_load_prediction(relative_compactness, surface_area, wall_area, roof_area, overall_height, orientation, glazing_area, glazing_area_distribution):
    features = [
        float(relative_compactness),
        float(surface_area),
        float(wall_area),
        float(roof_area),
        float(overall_height),
        float(orientation),
        float(glazing_area),
        float(glazing_area_distribution)
    ]

    heat_prediction = heat_model.predict([features])[0] if heat_model else None
    
    return heat_prediction


def cool_load_prediction(relative_compactness, surface_area, wall_area, roof_area, overall_height, orientation, glazing_area, glazing_area_distribution):
    features = [
        float(relative_compactness),
        float(surface_area),
        float(wall_area),
        float(roof_area),
        float(overall_height),
        float(orientation),
        float(glazing_area),
        float(glazing_area_distribution)
    ]

    cool_prediction = cool_model.predict([features])[0] if cool_model else None
    
    return cool_prediction


