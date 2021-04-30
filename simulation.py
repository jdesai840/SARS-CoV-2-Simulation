import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime
from matplotlib.animation import FuncAnimation
import time
from itertools import count

sns.set_theme(style='darkgrid')
sns.set_palette('Set3')

dates = [
    datetime(2020, 1, 4),
    datetime(2020, 2, 2),
    datetime(2020, 3, 3),
    datetime(2020, 4, 5),
    datetime(2020, 5, 4),
    datetime(2020, 6, 2),
    datetime(2020, 7, 5),
    datetime(2020, 8, 3),
    datetime(2020, 9, 5),
    datetime(2020, 10, 5),
    datetime(2020, 11, 7),
    datetime(2020, 12, 6),
    datetime(2021, 1, 4),
    datetime(2021, 2, 6),
    datetime(2021, 3, 7),
    datetime(2021, 4, 5)
]

ys = [
    [59, 53, 34, 17, 10, 6, 5, 4, 3, 2, .1, 1, 1, 1, .1, .1],
    [33, 26, 11, 11, 7, 7, 4, 5, 3, 2, 4, 4, 4, 4, 2, .5],
    [7, 13, 28, 35, 38, 33, 35, 33, 28, 33, 33, 28, 26, 21, 15, 10],
    [.1, 5, 14, 19, 29, 35, 38, 35, 38, 39, 34, 25, 22, 20, 18, 14],
    [.1, 3, 13, 17, 14, 16, 8, 8, 9, 5, 9, 8, 8, 7, 7, 8],
    [0, 0, .1, .1, 1, 3, 3, 3, 5, 5, 5, 5, 5, 4, 3, 3],
    [0, 0, 0, 0, 0, 0, .1, .1, 5, 6, 5, 5, 5, 4, 2, .1],
    [0, 0, 0, 0, .1, 1, 6, 11, 8, 4, .1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, .1, .3, 2, 3, 6, 7, 7, 8, 5, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, .1, 2, 5, 7, 8, 9, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 13, 22, 37, 50],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .1, .5, 1, 1, 2, 4]
]

twentyJ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .1, .5, 1, 1, 2, 4]
twentyI = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 13, 22, 37, 50]
twentyH = [0, 0, 0, 0, 0, 0, 0, 0, 0, .1, 2, 5, 7, 8, 9, 8]
twentyG = [0, 0, 0, 0, 0, 0, .1, .3, 2, 3, 6, 7, 7, 8, 5, 2]
twentyF = [0, 0, 0, 0, .1, 1, 6, 11, 8, 4, .1, 0, 0, 0, 0, 0]
twentyE = [0, 0, 0, 0, 0, 0, .1, .1, 5, 6, 5, 5, 5, 4, 2, .1]
twentyD = [0, 0, .1, .1, 1, 3, 3, 3, 5, 5, 5, 5, 5, 4, 3, 3]
twentyC = [.1, 3, 13, 17, 14, 16, 8, 8, 9, 5, 9, 8, 8, 7, 7, 8]
twentyB = [.1, 5, 14, 19, 29, 35, 38, 35, 38, 39, 34, 25, 22, 20, 18, 14]
twentyA = [7, 13, 28, 35, 38, 33, 35, 33, 28, 33, 33, 28, 26, 21, 15, 10]
nineteenB = [33, 26, 11, 11, 7, 7, 4, 5, 3, 2, 4, 4, 4, 4, 2, .5]
nineteenA = [59, 53, 34, 17, 10, 6, 5, 4, 3, 2, .1, 1, 1, 1, .1, .1]


strains = ['19A', '19B', '20A', '20B', '20C', '20D' '20E', '20F', '20G', '20H', '20I', '20J']
strainsrev = ['20J', '20I', '20H', '20G', '20F', '20E', '20D', '20C', '20B', '20A', '19B', '19A']
title = 'Relative Frequencies of SARS-CoV-2 Strains Worldwide since January 2020'


fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))
axes.set_ylim(0, 100)


x1, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12 = [], [], [], [], [], [], [], [], [], [], [], [], []

def animate(i):
    
    if i==0:
        axes.legend(loc='upper left', labels=['20J', '20I', '20H', '20G', '20F', '20E', '20D', '20C', '20B', '20A', '19B', '19A'])
    
    if i <= 15:
        x1.append(dates[i])
        y1.append(twentyJ[i])
        y2.append(twentyI[i])
        y3.append(twentyH[i])
        y4.append(twentyG[i])
        y5.append(twentyF[i])
        y6.append(twentyE[i])
        y7.append(twentyD[i])
        y8.append(twentyC[i])
        y9.append(twentyB[i])
        y10.append(twentyA[i])
        y11.append(nineteenB[i])
        y12.append(nineteenA[i])

        
        plt.stackplot(x1, y1, y2, y3, y4, y5,y6, y7, y8, y9, y10, y11, y12, alpha=1)
        plt.xlabel('Date')
        plt.ylabel('Relative Frequency (%)')
        plt.title(title)
        date_format = mpl_dates.DateFormatter('%b %y')
        plt.gca().xaxis.set_major_formatter(date_format)
        
    
    
anim = FuncAnimation(fig, animate, interval=1500)
plt.show()
