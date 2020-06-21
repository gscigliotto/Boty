
import numpy as np
import csv
from talib.abstract import *

import AlphaVeDataSrc as data
import json
import pandas as pd
import Setup as setup


from mpl_finance import candlestick_ohlc
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


dataSource = data.AlphaVeDataSrc()


#f = open("data_GGAL.csv", "w")
#f.write(dataSource.getDataCsv('GGAL',data.EnumFuncionPeriod.TIME_SERIES_WEEKLY,data.EnumInterval.NONE))
#f.close()

#dataResult = pd.read_csv("data_GGAL.csv")
#dataResult.fillna(method='ffill')

dataResult = dataSource.getData('GGAL',data.EnumFuncionPeriod.TIME_SERIES_WEEKLY,data.EnumInterval.NONE);






output = SMA(dataResult,timeperiod=5,price='close')
#output = SMA(dataResult)
print(output.array)




#dataResult['timestamp']= [mdates.strpdate2num(d) for d in dataResult['timestamp']]

dataResult['timestamp']= [matplotlib.dates.datestr2num(d) for d in dataResult['timestamp']]


quotes = [tuple(x) for x in dataResult[['timestamp','open','high','low','close']].values]




# Plot candlestick.
##########################
fig, ax = plt.subplots()
candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');
 
 
# Customize graph.
##########################
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('GGAL')
 
# Format time.
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
 
plt.gcf().autofmt_xdate()   # Beautify the x-labels
#plt.autoscale(tight=True)
#plt.show() 
# Save graph to file.
plt.savefig('mpl_finance-apple.png')
