import yfinance as yf

def get_stock(symbol, interval="1d", period="6mo"):

    data = yf.download(
        symbol,
        period=period,
        interval=interval
    )

    return data