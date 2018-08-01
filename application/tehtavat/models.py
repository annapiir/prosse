from application import db

class Tehtava(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pvm_luonti = db.Column(db.DateTime, default=db.func.current_timestamp())
    pvm_muokkaus = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    nimi = db.Column(db.String(144), nullable=False)
    kuvaus = db.Column(db.String(300), nullable=True)

    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus