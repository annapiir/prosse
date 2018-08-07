from application import db

class Kayttaja(db.Model):

    __tablename__ = "kayttaja"
  
    id = db.Column(db.Integer, primary_key=True)
    pvm_luonti = db.Column(db.DateTime, default=db.func.current_timestamp())
    pvm_muokkaus = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    kayttajan_nimi = db.Column(db.String(144), nullable=False)
    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

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