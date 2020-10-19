
from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,
    String, Table, Float,Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
import Setup as setup
from datetime import date

parametros = setup.Setup()
engine = parametros.getEngine()
Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()



class Ticker(Base):
    __tablename__ = 'ticker'
    id = Column(Integer, primary_key=True)
    ticker = Column(String(8), index=True, nullable=False)

    descripcion = Column(String(30))
    estados = relationship("Estado")


    def __init__(self, ticker,descripcion ,estados):
        self.ticker = ticker
        self.descripcion = descripcion
        self.estados =estados
        

    def __init__(self, ticker,descripcion):
        self.ticker = ticker
        self.descripcion = descripcion
        
        



class Estado(Base):
    __tablename__ = 'estado'
    id = Column(Integer, primary_key=True)
    tickerid =  Column(Integer, ForeignKey("ticker.id"))
    mediaRapida = Column(Float, nullable=False)
    mediaLenta = Column(Float, nullable=False)
    macd= Column(Float, nullable=False)
    macdsignal = Column(Float, nullable=False)
    macdhist = Column(Float, nullable=False)
    cumple = Column(Boolean,nullable=False)
    fecha_publicacion = Column(Date)

    def __init__(self, mediaRapida,mediaLenta,macd,macdsignal,macdhist,cumple,fecha_publicacion,tickerid):
        self.mediaRapida = mediaRapida
        self.mediaLenta = mediaLenta
        self.macd = macd
        self.macdsignal = macdhist
        self.macdhist =macdhist
        self.cumple =cumple
        self.fecha_publicacion = fecha_publicacion
        self.tickerid = tickerid



class Tarea(Base):
    __tablename__='tarea'
    id = Column(Integer, primary_key=True)
    NombreTarea = Column(String(10), index=True, nullable=False) 
    fechaEjecucion = Column(Date)
    inicio = Column(Date)
    fin = Column(Date)
    estadoEjecucion = Column(Boolean,nullable=False)
    def __init__(self,NombreTarea,fechaEjecucion,inicio,fin,estadoEjecucion):
        self.NombreTarea = NombreTarea
        self.fechaEjecucion = fechaEjecucion
        self.inicio = inicio
        self.fin = fin
        self.estadoEjecucion = estadoEjecucion

    def __init__(self,NombreTarea,estadoEjecucion):
        self.NombreTarea = NombreTarea
        self.estadoEjecucion = estadoEjecucion



Base.metadata.create_all(engine)

tarea = Tarea('SWING',False) 
session.add(tarea)



symbols = ['GGAL','YPF','BMA','PAM','LOMA','SUPV','BBAR','EDN','CEPU','CRESY','TEO','TGS','IRS','IRCP','TS','AAPL','KO','GOLD','INTC','AMZN','TSLA','MSFT','DIS','WMT','BABA','BBD','DESP','GOOGL','AUY','MELI','FB','XOM','PBR','GE','VALE','BAC','GLOB','CSCO','BA','NFLX','MCD','JPM','JNJ','C','AXP','GILD','IBM','MMM','AIG','RDS.B','CVX','LMT']
for ticket in symbols:
    tickerAlta = Ticker(ticket,'')
    session.add(tickerAlta)




session.commit()