#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd

def pygraph(booktoread):
    mdf = pd.read_excel(booktoread, sheet_name="Sheet1")
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
    filesaved = now.strftime("%Y-%m-%d-outage.png")
    plt.savefig(filesaved)
    return filesaved
    
    plt.show()
    #plt.savefig(now.strftime("%Y-%m-%d-outage.png"))
   


