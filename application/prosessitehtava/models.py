from application import db
from application.models import Base


class Prosessitehtava(Base):

    pvm_alku = db.Column(db.DateTime)
    pvm_loppu = db.Column(db.DateTime)
    pvm_kommentti = db.Column(db.DateTime)
    kommentti = db.Column(db.String(300), nullable=True)
    aloitettu = db.Column(db.Boolean, nullable=False)
    valmis = db.Column(db.Boolean, nullable=False)

    
    kuittaaja_alku_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id')) 
    kuittaaja_loppu_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'))
    kommentoija_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'))
    prosessi_id = db.Column(db.Integer, db.ForeignKey('prosessi.id'))
    tehtava_id = db.Column(db.Integer, db.ForeignKey('tehtava.id'))


    def __init__(self, prosessi_id, tehtava_id, pvm_alku, pvm_loppu):
        self.aloitettu = False
        self.valmis = False
        self.prosessi_id = prosessi_id
        self.tehtava_id = tehtava_id
        self.pvm_alku = pvm_alku
        self.pvm_loppu = pvm_loppu

class Tekija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pt_id = db.Column(db.Integer, db.ForeignKey('prosessitehtava.id'))
    tekija_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'))


    def __init__(self, pt_id, tekija_id):
        self.pt_id = pt_id
        self.tekija_id = tekija_id
