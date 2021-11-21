import yfinance as yf
import json
import pandas
import pickle
from pathlib import Path
import os.path

path = os.path.dirname(__file__)

with open(path + "/../../../data/finnhub/tickers.json") as json_file:
    tickers_json = json.load(json_file)

def harvest_exchange(exchange, out_dir="../../../data/yahoo"):

    Path(f"{path}/{out_dir}/{exchange}").mkdir(parents=True, exist_ok=True)

    tickers_json[exchange]

    num = len(tickers_json[exchange])
    save_step = 3000
    steps = int(num/save_step) +1

    print(f"{exchange} total: {num}")
    for i in range(steps):
        start = i*save_step
        end = i*save_step + save_step
        
        if end < num:
            print(f"{start} to {end}")
            df = yf.download(tickers_json[exchange][start:end], period='max', group_by = 'ticker')
        else:
            print(f"{start} to {num}")
            df = yf.download(tickers_json[exchange][start:], period='max', group_by = 'ticker')

        with open(f"{path}/{out_dir}/{exchange}/{i + 1}.pkl", 'wb') as outp:
            pickle.dump(df, outp, pickle.HIGHEST_PROTOCOL)


def harvest_exchanges():
    for exchange in tickers_json.keys():
        harvest_exchange(exchange)

harvest_exchange('US')


