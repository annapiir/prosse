from application import db
from application.models import Base

class Tehtava(Base):

    nimi = db.Column(db.String(144), nullable=False)
    kuvaus = db.Column(db.String(300), nullable=True)

    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus