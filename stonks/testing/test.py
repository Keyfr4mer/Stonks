import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.stonks.apis.alphavantage_api import AlphaVantage
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
import pickle
import os
import json
from collections import Counter

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

# yahoo("AAPL")
# test()

