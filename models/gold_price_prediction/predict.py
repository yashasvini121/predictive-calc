from models.gold_price_prediction.model import gold_price_prediction

def get_prediction(spx, uso, slv, eur_usd):
    # Call the function that makes the prediction using input features
    return gold_price_prediction(spx, uso, slv, eur_usd)
