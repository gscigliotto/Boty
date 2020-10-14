
from sqlalchemy import (create_engine, Column, Date, Integer, ForeignKey,
    String, Table, Float,Boolean)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import Setup as setup


parametros = setup.Setup()
engine = parametros.getEngine()
Base = declarative_base()






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


Base.metadata.create_all(engine)