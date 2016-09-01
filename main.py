#!/usr/bin/env python
import matplotlib
import os
import operator
import time
from yahoo_finance import Currency,Share,datetime

os.system('clear')

cur_list = ["EURUSD", "EURGBP", "USDGBP" ]
cur_list_str = '\t'.join(str(x) for x in cur_list)

TITLE = "DATE\t\t\t%s" % cur_list_str
ROWS, COLUMNS = os.popen('stty size', 'r').read().split()
WC = 0
cur_list_data = cur_list_data_new = list(0 for x in range(len(cur_list)))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def get_data(symbol):
    return Currency(symbol).get_rate()

# main()
while True:
    # Refresh every 1/2 COLUMNS
    if WC == 0 or WC > int(COLUMNS)/2 :
        WC = 1
        os.system('clear')
        print TITLE

    cur_list_data_old = cur_list_data
    time.sleep(3)
    cur_list_data = map(get_data, cur_list)
    cur_minus = map(operator.sub, [float(x) for x in cur_list_data], [float(x) for x in cur_list_data_old])

    WC += 1
    for x in cur_list_data:
        c3_data = [bcolors.OKGREEN + str(x) + bcolors.ENDC if cur_minus[cur_list_data.index(x)] >= 0 else bcolors.FAIL + str(x) + bcolors.ENDC for x in cur_list_data]
    c3 = "%s\t%s" % (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '\t'.join(str(x) for x in c3_data))
    print c3

import matplo
