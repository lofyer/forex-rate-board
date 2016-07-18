#!/usr/local/bin/python
import matplotlib
import time
from datetime import datetime
from yahoo_finance import Currency,Share

cur_list = ["EURUSD", "EURGBP", "USDGBP" ]
cur_list_str = '\t'.join(str(x) for x in cur_list)

TITLE = "DATE\t\t\t%s" % cur_list_str
BODY = ""

def get_data(symbol):
    return Currency(symbol).get_rate()

print TITLE

while True:
    cur_list_data_str = '\t'.join(str(x) for x in map(get_data, cur_list))
    print "%s\t%s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), cur_list_data_str)
    time.sleep(5)
