# -*- coding:utf-8 -*-
import csv
import io
import numpy
import pandas as pd
import test_draw

data = []




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
        if row[0] ==  '日期':
            continue
        data.append([row[0],float(row[1]),float(row[4]),float(row[2]),float(row[3]),int(row[6]),3481])
del data[0]
print data
df2 = pd.DataFrame(data, columns=['date','open','close','high','low','volume','code'])
print df2
test_draw.draw_candle(df2)
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

