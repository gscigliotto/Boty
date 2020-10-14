
import numpy as np

from talib.abstract import *

import AlphaVeDataSrc as data
import json
import pandas as pd
import Setup as setup
import GraphGenerator as GraphGen

from Service.tickerService import tickerService

from time import sleep


def ema(values, period): 
    values = np.array(values) 
    return pd.ewma(values, span=period)[-1] 


def analizarTickerSwing(ticker):

    dataResult = dataSource.getData(ticker,data.EnumFuncionPeriod.TIME_SERIES_DAILY,data.EnumInterval.NONE);

    #GENERAR IMAGENES
    #Gg = GraphGen.GraphGenerator()
    #Gg.generateGrph(dataResult,'GGAL', 'GGAL_0001')

    if dataResult.empty != True :
        mediaRapida = EMA(dataResult,timeperiod=11,price='close')
        mediaLenta = EMA(dataResult,timeperiod=20,price='close')

        macd, macdsignal, macdhist = MACD( dataResult["close"] , fastperiod=12, slowperiod=26, signalperiod=9)
        cumple = cumpleTendencia(ticker,dataResult,mediaRapida,mediaLenta,macd,macdsignal,macdhist)
        return mediaRapida,mediaLenta,macd,macdsignal,macdhist,cumple



def cumpleTendencia(simbolo,precios,mediaRapida,mediaLenta,macd,macdsignal,macdhist):
    
    print('UTLIMOS 3 RAPIDA')
    ultimosPrecios = precios.tail(3)
    
    
    precioCount = 0
    mediaRCount = 0
    mediaLcount = 0
    macdCount   = 0
    macdSigCount= 0
    mediaCount = 0
    
        
    #PRECIOS ANTERIORES
    precioAnt = 0
   
    j = macd.size -3
    for i in ultimosPrecios.index:

        if ultimosPrecios['close'][i] > precioAnt :
            
            precioCount = precioCount +1

        precioAnt = ultimosPrecios['close'][i]
       
        if mediaRapida[i] > mediaLenta[i] :
            mediaCount = mediaCount + 1
        else :
            mediaCount = mediaCount - 1


        if macdsignal[j] < macd[j] :
            macdCount = macdCount + 1
        else :
            macdCount = macdCount - 1
        j = j + 1

    if precioCount == 3 and  mediaCount ==3 and macdCount == 3:

        print ('TICKER: '+simbolo+' CUMPLE')
        return True
    else :
        return False


tickerservice = tickerService()
dataSource = data.AlphaVeDataSrc()
symbols = ['BBV']   
#symbols = ['GGAL','YPF','BMA','PAM','LOMA','SUPV','BBAR','EDN','CEPU','CRESY','TEO','TGS','IRS','IRCP','TS','AAPL','KO','GOLD','INTC','AMZN','TSLA','MSFT','DIS','WMT','BABA','BBD','DESP','GOOGL','AUY','MELI','FB','XOM','PBR','GE','VALE','BAC','GLOB','CSCO','BA','NFLX','MCD','JPM','JNJ','C','AXP','GILD','IBM','MMM','BBV','AIG','RDS.B','CVX','LMT']
#symbols = ['GGAL','YPF','BMA','PAM','LOMA']
imgName = ''
contikers = 0
for ticket in symbols:
    tickerservice.crearTickerSinoExiste(tickerName=ticket)
    tickerID = tickerservice.getIdByTicker(ticket)
    
    if contikers == 5 :
        sleep(65)
        contikers = 0
    mediaRapida,mediaLenta,macd,macdsignal,macdhist,cumple = analizarTickerSwing(ticket)
    tickerservice.registrarEstado(cumple,tickerID)
    contikers = contikers + 1




