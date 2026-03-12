import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from dloader import get_stock
from indicators import mAv, add_rsi
from decision import decide
from hill_climbing import hillclimbing

st.title("Stock Trading Dashboard")

sym = st.text_input("Enter Stock Symbol", "AAPL")

view = st.selectbox(
        "Select Graph View",
        ["Day-Wise", "Week-Wise", "Month-Wise"],
        key="view-selector"
    )

if st.button("Analyze"):

    if view == "Day-Wise":
        data = get_stock(sym, interval="1h", period="5d")

    elif view == "Week-Wise":
        data = get_stock(sym, interval="1d", period="1mo")

    else:
        data = get_stock(sym, interval="1d", period="6mo")
    
    if data.empty:
        st.error("No data found for this stock symbol.")
        st.stop()
    data = mAv(data)
    data = add_rsi(data)

    prices = data["Close"].squeeze().tolist()

    buy, sell, profit = hillclimbing(prices)

    decision = decide(data, buy, sell)

    st.write("AI Recommendation:", decision)

    buydate = data.index[buy]
    selldate = data.index[sell]

    st.write("Best Buy Day:", buydate.date())
    st.write("Best Sell Day:", selldate.date())
    st.write("Maximum Profit:", profit)


    fig, ax = plt.subplots()

    
    if view == "Day-Wise":

        recent = data.tail(5)

        ax.plot(recent.index, recent["Close"], label="Daily Price")
        ax.plot(recent.index, recent["MA"], label="Moving Average")

    
    elif view == "Week-Wise":

        recent = data.tail(30)

        ax.plot(recent.index, recent["Close"], label="Price (Last 30 Days)")
        ax.plot(recent.index, recent["MA"], label="Moving Average")

    
    else:

        monthly = data.resample("M").last()

        ax.plot(monthly.index, monthly["Close"], label="Monthly Close")

        if "MA" in monthly.columns:
            ax.plot(monthly.index, monthly["MA"], label="Monthly MA")


    prices_series = data["Close"].squeeze()

    ax.scatter(data.index[buy], prices_series.iloc[buy], label="BUY")
    ax.scatter(data.index[sell], prices_series.iloc[sell], label="SELL")

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_title("Stock Price Analysis")

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))

    plt.xticks(rotation=45)

    ax.grid(True)
    ax.legend()

    st.pyplot(fig)