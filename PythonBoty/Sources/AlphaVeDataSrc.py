import Setup as setup
import requests
import json
import pandas as pd
from datetime import date
from enum import Enum
from datetime import datetime

class AlphaVeDataSrc(object):

    def __init__(self):
        self.DataSetup =setup.Setup()
    
    def _getDataJson(self):
        data=''
        url=DataSetup.getURLDatos()+'&function=TIME_SERIES_INTRADAY&symbol=GGAL&interval=5min'
        response = requests.get(url, data=data)
        return response

    def _getDataCsv(self,symbol,funcionPeriod,interval):
        data=''

        if interval.value==0:
            inter=''
        else:
            inter='&interval='+interval.value
        
        url=self.DataSetup.getURLDatos()+'&function='+funcionPeriod.value+'&symbol='+symbol+inter+'&datatype=csv'
        response = requests.get(url, data=data)
        return response.text

    def getData(self,symbol,funcionPeriod,interval):
        dirName = self.DataSetup.getDataDir()
        fileName=dirName+"data_"+symbol+"_"+funcionPeriod.value+"_"+str(interval)+".csv"

        self.write(self._getDataCsv(symbol,funcionPeriod,interval),fileName)

        dataResult = pd.read_csv(fileName, index_col=0, parse_dates=True,infer_datetime_format=False) 
        #ESTE FILTRO SI FUNCIONA
        #dataResult=dataResult.loc['2020-10-09':'2020-01-01']
        dataResult.sort_index(inplace=True)
        dataResult.fillna(method='ffill')
        return dataResult

    def write(self,data,filename):
        f = open(filename, "w")
        f.write(data)
        f.close()

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


