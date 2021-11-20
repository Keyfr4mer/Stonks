import pandas as pd
import finnhub
import time
import json

from pandas.core.base import DataError
from pandas.core.frame import DataFrame


def download_tickers(filename = 'tickers.json'):
    #list of available exchanges

    df=pd.read_html("https://docs.google.com/spreadsheets/d/1I3pBxjfXB056-g_JYf_6o3Rns3BV2kMGG1nCatb91ls/edit#gid=0")
    df1=df[0]
    exc=df1.loc[:,"A"].dropna()

    exclist=[]
    for i in exc:
        exclist.append(str(i))
    exclist=exclist[1:] #take out "name" from the list


    #retrieve tickers from every exchange available
    data= {}
    finnhub_client = finnhub.Client(api_key="c6btimaad3idja5prvqg")
    for exchange in exclist:
        tickers=[]
        listofdicts=finnhub_client.stock_symbols(exchange)
        for dicts in listofdicts:
            tickers.append(dicts['symbol'])
        time.sleep(0.5)
        data[exchange] = tickers

    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4)

download_tickers()