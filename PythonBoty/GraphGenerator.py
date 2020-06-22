
import mplfinance as  mpf
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


class GraphGenerator(object):
    def generateGrph(self, dataResult,symbol,imgFile):
        #dataResult['timestamp']= [mdates.strpdate2num(d) for d in dataResult['timestamp']]
       # dataResult['timestamp']= [matplotlib.dates.datestr2num(d) for d in dataResult['timestamp']]
        #quotes = [tuple(x) for x in dataResult[['timestamp','open','high','low','close']].values]

        dataResult.rename(columns = {'open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'}, inplace = True) 


        ## Plot candlestick.
        ###########################
        #fig, ax = plt.subplots()
        #candlestick_ohlc(ax, quotes, width=0.5, colorup='g', colordown='r');
 
 
        ## Customize graph.
        ###########################
        #plt.xlabel('Date')
        #plt.ylabel('Price')
        #plt.title('GGAL')
 
        ## Format time.
        #ax.xaxis_date()
        #ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
 
        #plt.gcf().autofmt_xdate()   # Beautify the x-labels
   
        #plt.savefig('mpl_finance-apple.png')
        mpf.plot(dataResult, type = 'candle', style = 'charles',
            title = symbol,
            ylabel = 'Price ($)',
            ylabel_lower='Shares \nTraded',
            volume = True, 
            mav = (3,6,9), 
            savefig = imgFile+'.png',datetime_format='%d-%m-%Y')

