#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

mdf = pd.read_excel('Books.xls', sheet_name="Sheet1")
menMeans = mdf['mins']
menMeans = tuple(menMeans.values)

quarters = mdf['quarter']
quarters = tuple(quarters.values)


N = 4
#menMeans = (20, 35, 30, 35)
ind = np.arange(N)
width = 0.30

p1 = plt.bar(ind, menMeans, width)

plt.ylabel('Outage Minutes')
plt.title('Outage Minutes per Quater')
plt.xticks(ind, (quarters))
#plt.xticks(ind, ('Q1', 'Q2', 'Q3', 'Q4'))
plt.yticks(np.arange(0, 201, 15))
plt.legend((p1[0],), ('Minutes',))

now = datetime.datetime.now()
plt.savefig(now.strftime("%Y-%m-%d-outage.png"))


