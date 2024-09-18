import csv
import matplotlib.pyplot as plt
from datetime import datetime
import pandas

data=pandas.read_csv("task9.csv",header=0)
xtime=data.iloc[:,0].values
y1=data.iloc[:,1].values
y2=data.iloc[:,2].values
y3=data.iloc[:,3].values
y4=data.iloc[:,4].values
y5=data.iloc[:,5].values
y6=data.iloc[:,6].values



plt.plot(xtime,y1, label="meta")

plt.plot(xtime,y2, label="aapl")

plt.plot(xtime,y3, label="amzn")

plt.plot(xtime,y4, label="ntfx")

plt.plot(xtime,y5, label="nvda")

plt.plot(xtime,y6, label="googl")
plt.gca().set_xticklabels([])
plt.legend()
plt.show()
#,META,AAPL,AMZN,NFLX,NVDA,GOOGL