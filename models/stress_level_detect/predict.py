# predict.py
from models.stress_level_detect.model import stress_level_prediction

def get_prediction(age, freq_no_purpose, freq_distracted, restless, worry_level, difficulty_concentrating,
                   compare_to_successful_people, feelings_about_comparisons, freq_seeking_validation,
                   freq_feeling_depressed, interest_fluctuation, sleep_issues):
    """
    Gets the stress prediction and provides advice based on predicted stress levels.
    """
    prediction, confidence = stress_level_prediction(age, freq_no_purpose, freq_distracted, restless, worry_level,
                                                     difficulty_concentrating, compare_to_successful_people,
                                                     feelings_about_comparisons, freq_seeking_validation,
                                                     freq_feeling_depressed, interest_fluctuation, sleep_issues)

    advice = ""

    # Provide detailed advice based on stress levels and confidence
    if prediction == 0:
        advice = f"You are experiencing mild stress (Confidence: {confidence:.2f}). " \
                 "Maintain a balanced lifestyle, engage in relaxing activities like reading or light exercise."
    elif prediction == 1:
        advice = f"You have moderate stress (Confidence: {confidence:.2f}). " \
                 "Consider practicing stress-relief techniques like mindfulness, walking, or deep breathing."
    elif prediction == 2:
        advice = f"You are experiencing high stress levels (Confidence: {confidence:.2f}). " \
                 "It's important to seek professional advice, adopt strong coping strategies, and take breaks."

    return advice
