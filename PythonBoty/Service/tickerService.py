import Setup as setup
from models.model import Ticker,Estado
from sqlalchemy.orm import sessionmaker
from datetime import date



class tickerService(object):
    def __init__(self, *args, **kwargs):
        self.parametros = setup.Setup()
        self.engine = self.parametros.getEngine()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()        

    def crearTicker(self,tickerName,descripcion):
        ticker = Ticker(tickerName,descripcion) 
        self.session.add(ticker)
        self.session.commit()

    def buscarTicker(self,tickerName):
        return self.session.query(Ticker).filter(Ticker.ticker==tickerName)

    def getIdByTicker(self,tickerName):
        return self.session.query(Ticker).filter(Ticker.ticker==tickerName).first().id

    def crearTickerSinoExiste(self,tickerName):
        if self.session.query(Ticker).filter(Ticker.ticker==tickerName).count() < 1:
            self.crearTicker(tickerName,' ')

    def registrarEstado(self,cumple,tickerID):
        estado = Estado(0.0,0.0,0.0,0.0,0.0,cumple,date.today(),tickerID)
        self.session.add(estado)
        self.session.commit()

    