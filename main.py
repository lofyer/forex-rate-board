#!/usr/bin/env python
import matplotlib
from yahoo_finance import Currency,Share

cur_list = {"EURUSD":"", "EURGBP":"", "USDGBP":""}

for cur in cur_list.keys():
    cur_list[cur] = Currency(cur).get_rate()

print cur_list
