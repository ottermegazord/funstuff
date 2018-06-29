import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
import pandas as pd

def bacteriaExtract(df, BacteriaId):

    dout = pd.DataFrame()

    for i in range (0, df.shape[0]):
        if df['BacteriaId'].iloc[i] == BacteriaId:
            #print df.iloc[i]
            dout = dout.append(df.iloc[i], ignore_index=True)

    return dout

data = '/Users/idaly666/PycharmProjects/funstuff/onexi/data/data1.csv'
df = pd.read_csv(data)

bac0 = bacteriaExtract(df, 0)
bac1 = bacteriaExtract(df, 1)
bac2 = bacteriaExtract(df, 2)

ax = plt.subplot(111)
ax.bar(bac0['Frame'].iloc[0:13]-0.2, bac0['X'].iloc[0:13],width=0.2,color='b',align='center', linewidth=6.0)
ax.bar(bac1['Frame'].iloc[0:13], bac1['X'].iloc[0:13],width=0.2,color='g',align='center', linewidth=6.0)
ax.bar(bac2['Frame'].iloc[0:13]+0.2, bac2['X'].iloc[0:13],width=0.2,color='r',align='center', linewidth=6.0)

plt.show()