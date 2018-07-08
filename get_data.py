# -*- coding:utf-8 -*-
import csv
import io

data = []

with open('3481.csv', mode='r', encoding='utf-8') as f: 
    reader = csv.reader(f)
    for row in reader:
        print(row)
