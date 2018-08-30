from application import db
from application.models import Base
from flask_login import current_user
from application.prosessitehtava.models import Prosessitehtava

from sqlalchemy.sql import text

class Kayttaja(Base):

    __tablename__ = "kayttaja"

    kayttajan_nimi = db.Column(db.String(144), nullable=False)
    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    prosessit = db.relationship("Prosessi", backref='kayttaja', lazy=True)
    pt_kommentoija = db.relationship("Prosessitehtava", backref='kommentoija', foreign_keys=[Prosessitehtava.kommentoija_id], lazy=True)
    pt_kuittaaja_alku = db.relationship("Prosessitehtava", backref='kuittaaja_alku', foreign_keys=[Prosessitehtava.kuittaaja_alku_id], lazy=True)
    pt_kuittaaja_loppu = db.relationship("Prosessitehtava", backref='kuittaaja_loppu', foreign_keys=[Prosessitehtava.kuittaaja_loppu_id], lazy=True)
    tekija = db.relationship("Tekija", backref='tekija', lazy=True)

    def __init__(self, kayttajan_nimi, tunnus, salasana):
        self.kayttajan_nimi = kayttajan_nimi
        self.tunnus = tunnus
        self.salasana = salasana

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def kayttaja_tunnus(self):
        return self.tunnus

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def montako_prosessia_kayttajalla():

            if current_user.get_id() is None:
                return "Ei käyttäjää"
            else:
                kayttaja_id = current_user.get_id()
                stmt = text("SELECT Kayttaja.id as id, Kayttaja.kayttajan_nimi as nimi, COUNT(Prosessi.id) as lkm FROM Kayttaja"
                            " LEFT JOIN Prosessi ON Prosessi.owner_id = Kayttaja.id"
                            " WHERE Kayttaja.id = :kayttaja_id"
                            " GROUP BY Kayttaja.id").params(kayttaja_id=kayttaja_id)

                res = db.engine.execute(stmt)

                return res
    
    @staticmethod
    def kayttajan_prosessit():
        if current_user.get_id() is None:
            return "Ei käyttäjää"
        else:
            kayttaja_id = current_user.get_id()
            stmt = text("SELECT Prosessi.id as prosessi_id, Prosessi.prosessin_nimi as prosessin_nimi FROM Prosessi"
                        " LEFT JOIN Kayttaja ON Prosessi.owner_id = Kayttaja.id"
                        " WHERE Kayttaja.id = :kayttaja_id").params(kayttaja_id=kayttaja_id)
            
            res = db.engine.execute(stmt)

            prosessit = []
            
            for prosessi in res:
                prosessit.append(prosessi)

            return prosessit
    

    @staticmethod
    def kayttajan_keskeneraiset_tehtavat_lkm():
        if current_user.get_id() is None:
            return "Ei käyttäjää"
        else:
            kayttaja_id = current_user.get_id()
            stmt = text("SELECT COUNT(Prosessitehtava.id) as lkm FROM Prosessitehtava"
                        " JOIN Tekija ON Tekija.pt_id = Prosessitehtava.id"
                        " WHERE Tekija.tekija_id = :kayttaja"
                        " AND Prosessitehtava.aloitettu"
                        " AND NOT Prosessitehtava.valmis").params(kayttaja=kayttaja_id)
            
            res = db.engine.execute(stmt)

            return res

