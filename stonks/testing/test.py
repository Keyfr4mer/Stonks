from alphavantage_api import AlphaVantage
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
import pickle

def yahoo(ticker):
    msft = yf.Ticker(ticker)
    df = msft.history(period="max")
    print(df)
    df['MA'] = df['Close'].rolling(window=5).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA'], mode='lines', name='MA'))
    fig.show()


def alpha():
    av = AlphaVantage('BCHSP7W9RIPI6UMS')

    df = pd.DataFrame(av.get_daily_adjusted('AAPL', 'full'))
    print(df.head())
    df['MA'] = df['Close'].rolling(window=50).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close'))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MA'], mode='lines', name='MA'))
    fig.show()

with open(r"./data/US_1.pkl", "rb") as input_file:
    df = pickle.load(input_file)

def test():
    tickers = []
    for column in df.columns:
        if column[0] not in tickers:
            tickers.append(column[0])

    print(tickers)
    print(len(tickers))

    show = 5
    
    fig = go.Figure()

    for ticker in tickers[10:50]:
        to_show = df[ticker]
        to_show['MA'] = to_show['Close'].rolling(window=50).mean()

        fig.add_trace(go.Scatter(x=to_show.index, y=to_show['Close'], mode='lines', name=ticker +' Close'))
        fig.add_trace(go.Scatter(x=to_show.index, y=to_show['MA'], mode='lines', name=ticker+ ' MA'))
    fig.show()

# yahoo("AAPL")
test()
