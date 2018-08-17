from application import db
from application.models import Base
from flask_login import current_user

from sqlalchemy.sql import text

class Kayttaja(Base):

    __tablename__ = "kayttaja"

    kayttajan_nimi = db.Column(db.String(144), nullable=False)
    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    prosessit = db.relationship("Prosessi", backref='kayttaja', lazy=True)

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