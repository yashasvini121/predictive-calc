def bitcoin_price_predictor(current_price, moving_average, market_sentiment):
    if current_price > moving_average and market_sentiment == "positive":
        return "Bitcoin price will rise"
    else:
        return "Bitcoin price will fall"
