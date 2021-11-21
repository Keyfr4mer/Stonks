import os
import sys
import pickle
import json
from typing import Counter
from collections import Counter
import plotly.graph_objects as go
import pandas as pd

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(currentdir)))
sys.path.append(parentdir)

def generate_info_json():
    info_json = {}
    for subdir, dirs, files in os.walk(parentdir + "/data/yahoo"):
        try:
            exchange = subdir.split("yahoo\\")[1]
        except:
            continue

        for file in files:
            if file.endswith(".pkl"):
                with open(os.path.join(subdir, file), "rb") as input_file:
                    df = pickle.load(input_file)
                    print(exchange + "/" + file)
                    tickers = []
                    for column in df.columns:
                        if column[0] not in tickers:
                            tickers.append(column[0])
                    info_json[file] = tickers

    with open(os.path.join(subdir, "info.json"), "w") as output_file:
        json.dump(info_json, output_file, indent=4)


def get_tickers():
    with open(os.path.join(parentdir + "/data/yahoo/US", "info.json"), "rb") as input_file:
            info_json = json.load(input_file)

    tickers = []
    for key in info_json.keys():
        
        tickers.extend(info_json[key])

    counts = Counter(tickers).items()

    for ticker, count in counts:
        if count > 1:
            print(ticker+ ": " + str(count))


def get_ticker(ticker, show_figure=True):
    with open(os.path.join(parentdir + "/data/yahoo/US", "info.json"), "rb") as input_file:
            info_json = json.load(input_file)

    for key in info_json.keys():
        if ticker in info_json[key]:
            df_file = os.path.join(parentdir + "/data/yahoo/US", key)
            with open(df_file, "rb") as input_file:
                df = pickle.load(input_file)
                to_show = df[ticker]

    if show_figure:
        fig = go.Figure()

        to_show['MA'] = to_show['Close'].rolling(window=50).mean()

        fig.add_trace(go.Scatter(x=to_show.index, y=to_show['Close'], mode='lines', name=ticker +' Close'))
        fig.add_trace(go.Scatter(x=to_show.index, y=to_show['MA'], mode='lines', name=ticker+ ' MA'))
        fig.show()
    
    return to_show