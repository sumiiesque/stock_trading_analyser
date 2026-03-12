import ta

def mAv(data):
    data["MA"]=data["Close"].rolling(20).mean()
    return data

def add_rsi(data):
    closeprices=data["Close"].squeeze()
    data["RSI"]=ta.momentum.RSIIndicator(closeprices).rsi()
    return data