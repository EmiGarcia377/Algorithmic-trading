from statsmodels.regression.rolling import RollingOLS
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import pandas_ta
import warnings

warnings.filterwarnings("ignore")

sp500 = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
        attrs={"id": "constituents"},
        header=0,
        storage_options={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    )[0]

sp500["Symbol"] = sp500["Symbol"].str.replace(".", "-")

symbols_list = sp500["Symbol"].unique().tolist()

end_date = '2025-12-29'

start_date = pd.to_datetime(end_date) - pd.DateOffset(365*8)

df = yf.download(tickers=symbols_list, start=start_date, end=end_date)