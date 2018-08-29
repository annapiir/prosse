from application import db
from application.models import Base

from sqlalchemy.sql import text

class Prosessi(Base):

    prosessin_nimi = db.Column(db.String(144), nullable=False)
    pvm_alku = db.Column(db.DateTime)
    pvm_loppu = db.Column(db.DateTime)

    owner_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)

    prosessitehtavat = db.relationship("Prosessitehtava", backref='prosessi', lazy=True)

    db.Index('idx_prosessi', prosessin_nimi, owner_id)

    def __init__(self, prosessin_nimi, owner_id, pvm_alku, pvm_loppu):
        self.prosessin_nimi = prosessin_nimi
        self.owner_id = owner_id
        self.pvm_alku = pvm_alku
        self.pvm_loppu = pvm_loppu

    @staticmethod
    def listaa_prosessin_tehtavat(prosessi_id):

        stmt = text("SELECT Tehtava.id as id, Tehtava.nimi as nimi, Tehtava.kuvaus as kuvaus FROM Tehtava"
                    " INNER JOIN Prosessitehtava ON Prosessitehtava.prosessi_id = :prosessi_id").params(prosessi_id=prosessi_id)

        res = db.engine.execute(stmt)

        return res