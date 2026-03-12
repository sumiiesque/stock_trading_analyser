📈 Stock Trading Analyzer
An interactive stock market analysis dashboard that combines technical indicators and optimization algorithms to identify optimal buy and sell trading opportunities.
The system fetches real-time stock data, analyzes market trends using indicators such as RSI and Moving Average, and applies a hill climbing optimization algorithm to determine the most profitable trading points.
🚀 Features
📊 Real-time stock data fetching
📈 Interactive stock price visualization
📉 Technical indicators (RSI & Moving Average)
🤖 AI-based trading recommendation (BUY / SELL / HOLD)
⚡ Hill Climbing optimization for maximum profit
💰 Investment simulation for evaluating strategies
⏱ Multiple time-frame analysis
Hourly (intraday)
Daily
Monthly
🖥 Interactive dashboard using Streamlit
🧠 Algorithms Used
Hill Climbing Optimization
The system uses a hill climbing algorithm to search for the best buy–sell pair in historical stock prices by maximizing profit.
Profit is calculated as:
Profit = Selling Price − Buying Price
The algorithm iteratively explores possible buy/sell pairs and keeps the combination that produces the maximum profit.
🛠 Tech Stack
Programming Language
Python
Libraries
Streamlit (Dashboard UI)
Pandas / NumPy (Data processing)
Matplotlib (Visualization)
yfinance (Stock market data)
TA library (Technical indicators)
Many modern stock analysis tools combine similar techniques such as technical indicators and data visualization to analyze market trends.
📊 How It Works
Data Fetching
Stock data is fetched from Yahoo Finance API.
Technical Analysis
RSI and Moving Average indicators are calculated.
Optimization
Hill climbing algorithm finds the optimal buy/sell days.
Decision Engine
Combines indicators and optimization results to generate:
BUY
SELL
HOLD signals.
Visualization
Displays price trends, moving averages, and buy/sell points in an interactive dashboard.
📷 Example Dashboard Output
The dashboard displays:
Stock price trends
Moving average lines
Buy and sell markers
Trading recommendation
Profit simulation for a given investment
⚙️ Installation
Clone the repository:
git clone https://github.com/sumiiesque/stock_trading_analyser.git
Navigate to the project directory:
cd stock_trading_analyser
Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py
📁 Project Structure
stock_trading_analyser/
│
├── app.py              # Streamlit dashboard
├── dloader.py          # Stock data fetching
├── indicators.py       # RSI and Moving Average calculations
├── decision.py         # Trading signal logic
├── hill_climbing.py    # Optimization algorithm
│
├── requirements.txt
└── README.md
🔮 Future Improvements
Add more technical indicators (MACD, Bollinger Bands)
Integrate machine learning price prediction
Add multi-stock comparison
Deploy dashboard on cloud (AWS / Streamlit Cloud)
Implement portfolio optimization
