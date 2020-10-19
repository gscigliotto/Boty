
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
      #  mc = mpf.make_marketcolors( mavcolors=['r','g','g'])

        plt.rcParams['figure.figsize'] = [15.0, 15.0]
        plt.rcParams['figure.dpi'] = 140
        mc = mpf.make_marketcolors(up='g',down='r')


        mvcolors=mpf.make_mpf_style(base_mpl_style='classic' ,marketcolors=mc , mavcolors=['#1f77b4','#ff7f0e','#2ca02c'])

        kwargs = dict(type='candle',mav=(9,20,130),volume=True)
        #figratio=(11,8),figscale=0.85
        #output,macd, macdsignal, macdhist
        apdict = mpf.make_addplot(dataResult['Close'])



        mpf.plot(dataResult, **kwargs, style =mvcolors,
            title = symbol,
            ylabel = 'Precio',
            ylabel_lower='',
            savefig = imgFile+'.png',datetime_format='%d-%m-%Y',addplot=apdict)
        



