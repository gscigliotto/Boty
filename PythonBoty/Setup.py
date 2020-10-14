from sqlalchemy import create_engine

class Setup(object):

    def __init__(self):
        self._URL ="https://www.alphavantage.co/query?apikey="
        self._API_KEY="S1FTT3LUPIIY2984"
        self._DATA_DIR ="DATA/"
        self._DATA_BD = "DB/swing.db"

 
    def getURLDatos(self):
        return self._URL+self._API_KEY
    
    def getDataDir(self):
        return self._DATA_DIR

    def getDataDBDir(self):
        return self._DATA_DIR+self._DATA_BD

    def getEngine(self):
        return create_engine('sqlite:///'+self.getDataDBDir(), echo=True)


