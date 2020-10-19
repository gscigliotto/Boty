import Setup as setup
from models.model import Tarea
from sqlalchemy.orm import sessionmaker
from datetime import date


class ejecucionService (object):
    def __init__(self, *args, **kwargs):
        self.parametros = setup.Setup()
        self.engine = self.parametros.getEngine()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session() 

    def listarTareas(self):
        return self.session.query(Tarea).all()


