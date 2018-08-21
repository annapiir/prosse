from application import db
from application.models import Base

class Prosessitehtava(Base):

    pvm_alku = db.Column(db.DateTime)
    pvm_loppu = db.Column(db.DateTime)
    pvm_kommentti = db.Column(db.DateTime)
    kommentti = db.Column(db.String(300))
    aloitettu = db.Column(db.Boolean, nullable=False)
    valmis = db.Column(db.Boolean, nullable=False)

    
    kuittaaja_alku_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id')) 
    kuittaaja_loppu_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'))
    kommentoija_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'))
    prosessi_id = db.Column(db.Integer, db.ForeignKey('prosessi.id'))
    tehtava_id = db.Column(db.Integer, db.ForeignKey('tehtava.id'))


    def __init__(self, prosessi_id, tehtava_id):
        self.aloitettu = False
        self.valmis = False
        self.prosessi_id = prosessi_id
        self.tehtava_id = tehtava_id


