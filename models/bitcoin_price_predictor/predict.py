from models.bitcoin_price_predictor.model import bitcoin_price_predictor

def get_prediction(current_price, moving_average, market_sentiment):
    return bitcoin_price_predictor(current_price, moving_average, market_sentiment)
