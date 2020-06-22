import Setup as setup
import requests
import json
import pandas as pd
from datetime import date
from enum import Enum
from datetime import datetime

class AlphaVeDataSrc(object):
    def _getDataJson(self):
        DataSetup =setup.Setup()
        url=DataSetup.getURLDatos()+'&function=TIME_SERIES_INTRADAY&symbol=GGAL&interval=5min'
        data=''
        response = requests.get(url, data=data)
        return response

    def _getDataCsv(self,symbol,funcionPeriod,interval):
        if interval.value==0:
            inter=''
        else:
            inter='&interval='+interval.value
        DataSetup =setup.Setup()
        url=DataSetup.getURLDatos()+'&function='+funcionPeriod.value+'&symbol='+symbol+inter+'&datatype=csv'
        data=''
        response = requests.get(url, data=data)
        return response.text

    def getData(self,symbol,funcionPeriod,interval):
        fileName="data_"+symbol+"_"+funcionPeriod.value+"_"+str(interval)+".csv"
        
        f = open(fileName, "w")
        f.write(self._getDataCsv('GGAL',funcionPeriod,interval))
        f.close()
        dataResult = pd.read_csv(fileName, index_col=0, parse_dates=True,infer_datetime_format=False) #index_col=0
        #dataResult['timestamp']= [datetime.strptime(d, '%Y-%m-%d') for d in dataResult['timestamp']]
       # dataResult['periodo'] = dataResult['timestamp']
        #dataResult[dataResult['timestamp'] > pd.Timestamp(date(2020,5,1))]
        #dataResult.set_index('timestamp')
        #dataResult=dataResult.loc[date(year=2020,month=1,day=1):date(year=2000,month=1,day=1)].head()
        #dataResult = dataResult.between_time (date(year=2000,month=1,day=1), date(year=2020,month=1,day=1))
        #dataResult = dataResult.between_time ('2020-01-01', '2020-06-10')
        dataResult=dataResult.loc['2020-06-19':'2020-01-01']
        dataResult.sort_index(inplace=True)
        dataResult.fillna(method='ffill')
        
        
        return dataResult


class EnumFuncionPeriod(Enum):
    TIME_SERIES_INTRADAY="TIME_SERIES_INTRADAY"
    TIME_SERIES_DAILY="TIME_SERIES_DAILY"
    TIME_SERIES_DAILY_ADJUSTED="TIME_SERIES_DAILY_ADJUSTED"
    TIME_SERIES_WEEKLY="TIME_SERIES_WEEKLY"
    TIME_SERIES_WEEKLY_ADJUSTED="TIME_SERIES_WEEKLY_ADJUSTED"
    TIME_SERIES_MONTHLY="TIME_SERIES_MONTHLY"
    TIME_SERIES_MONTHLY_ADJUSTED="TIME_SERIES_MONTHLY_ADJUSTED"


class EnumInterval(Enum):
    ONE="1min"
    FIVE="5min"
    QUARTER="15min"
    HALF="30min"
    HOUR="60min"
    NONE=0
