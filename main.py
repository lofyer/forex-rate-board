#!/usr/local/bin/python
import matplotlib
import time
from yahoo_finance import Currency,Share

def get_data(symbol):
    return Currency(symbol).get_rate()

cur_list = ["EURUSD", "EURGBP", "USDGBP"]


print cur_list
while True:
    cur_list_data = map(get_data, cur_list)
    print cur_list_data
    time.sleep(5)
