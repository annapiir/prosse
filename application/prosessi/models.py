from application import db

class Prosessi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pvm_luonti = db.Column(db.DateTime, default=db.func.current_timestamp())
    pvm_muokkaus = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    prosessin_nimi = db.Column(db.String(144), nullable=False)
    pvm_alku = db.Column(db.DateTime)
    pvm_loppu = db.Column(db.DateTime)

    owner_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)

    def __init__(self, prosessin_nimi, owner_id, pvm_alku, pvm_loppu):
        self.prosessin_nimi = prosessin_nimi
        self.owner_id = owner_id
        self.pvm_alku = pvm_alku
        self.pvm_loppu = pvm_loppu