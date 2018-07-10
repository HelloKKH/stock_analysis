# -*- coding:utf-8 -*-
import csv
import io
import numpy
import pandas as pd

data = []
data1 = [4,5,6]
data2 = [7,8,9]
data.append(data1)
data.append(data2)
print(data)

with open('3481.csv', mode='r') as f:
    '''
    date = []
    open = []
    close = []
    high = []
    low = []
    vol = []
    '''
    reader = csv.reader(f)
    for row in reader:
        '''
        date.append(row[0])
        open.append(row[1])
        high.append(row[2])
        low.append(row[3])
        close.append(row[4])
        vol.append(row[6])
        '''
'''
print open
del open[0]
del date[0]
del high[0]
del low[0]
del close[0]
del vol[0]
open = [float(i) for i in open]
open = [float(i) for i in high]
open = [float(i) for i in low]
open = [float(i) for i in close]
print open
'''
