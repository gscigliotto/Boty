
import numpy as np

from talib.abstract import *

import AlphaVeDataSrc as data
import json
import pandas as pd
import Setup as setup
import GraphGenerator as GraphGen




dataSource = data.AlphaVeDataSrc()


#f = open("data_GGAL.csv", "w")
#f.write(dataSource.getDataCsv('GGAL',data.EnumFuncionPeriod.TIME_SERIES_WEEKLY,data.EnumInterval.NONE))
#f.close()

#dataResult = pd.read_csv("data_GGAL.csv")
#dataResult.fillna(method='ffill')

symbol = 'GGAL'
imgName = ''

dataResult = dataSource.getData('GGAL',data.EnumFuncionPeriod.TIME_SERIES_WEEKLY,data.EnumInterval.NONE);


Gg = GraphGen.GraphGenerator()

Gg.generateGrph(dataResult,'GGAL', 'GGAL_0001')


output = SMA(dataResult,timeperiod=5,price='Close')
#output = SMA(dataResult)
print(output.array)