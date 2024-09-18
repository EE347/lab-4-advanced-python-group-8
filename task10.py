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

myticks = ["2023-11", "2024-01", "2024-03", "2024-05", "2024-07", "2024-09"]

plt.plot(xtime,y1,color='b', label="meta")

plt.plot(xtime,y2,color='tab:gray', label="aapl")

plt.plot(xtime,y3, color='k',label="amzn")

plt.plot(xtime,y4, color='r', label="ntfx")

plt.plot(xtime,y5, color='g',label="nvda")

plt.plot(xtime,y6, color='tab:orange',label="googl")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.title("FAANING Performance")

plt.legend()
plt.show()
#,META,AAPL,AMZN,NFLX,NVDA,GOOGL