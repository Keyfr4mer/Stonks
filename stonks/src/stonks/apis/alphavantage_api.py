import requests
from datetime import datetime
import pandas as pd

#BCHSP7W9RIPI6UMS
class AlphaVantage:
    _API_URL = 'https://www.alphavantage.co/query?'

    def __init__(self, apikey):
        self.apikey = apikey

    def get_daily_adjusted(self, symbol, outputsize):
        params = {
        'apikey': self.apikey,
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'outputsize': outputsize,
        }

        api_result = requests.get(self._API_URL, params)
        api_response = api_result.json()
        time_series = api_response['Time Series (Daily)']
        dates = time_series.keys()

        data = []
        for date in dates:
            open = float(time_series[date]['1. open'])
            high = float(time_series[date]['2. high'])
            low = float(time_series[date]['3. low'])
            close = float(time_series[date]['4. close'])
            adjusted_close = float(time_series[date]['5. adjusted close'])
            volume = int(time_series[date]['6. volume'])
            dividend_amount = float(time_series[date]['7. dividend amount'])
            split_coefficient = float(time_series[date]['8. split coefficient'])    

            d = {'Open': open, 'High': high, 'Low': low, 'Close': adjusted_close, 'Volume': volume, 'Date': date}
            data.append(d)
        return data[::-1]