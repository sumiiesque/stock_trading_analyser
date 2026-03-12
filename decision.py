def decide(data, buy, sell):

    rsi = data["RSI"].iloc[-1]
    price = data["Close"].iloc[-1]
    ma = data["MA"].iloc[-1]

    last_index = len(data) - 1

    if last_index == buy:
        return "BUY"

    elif last_index == sell:
        return "SELL"

    elif rsi < 30 and price > ma:
        return "BUY"

    elif rsi > 70 and price < ma:
        return "SELL"

    else:
        return "HOLD"