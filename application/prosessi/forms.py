from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, validators
  

class ProsessiMuokkausLomake(FlaskForm):
    prosessin_nimi = StringField("Prosessin nimi",
        [validators.Length(min=2, message="Nimen pitää olla vähintään 2 merkkiä")])
    pvm_alku = DateField("Alkaa", format='%d.%m.%Y')
    pvm_loppu = DateField("Loppuu", format='%d.%m.%Y')
    tallenna = SubmitField("Tallenna")

    class Meta:
        csrf = False

class ProsessiLisaysLomake(FlaskForm):
    prosessin_nimi = StringField("Prosessin nimi",
        [validators.Length(min=2, message="Nimen pitää olla vähintään 2 merkkiä")])
    pvm_alku = DateField("Alkaa", format='%d.%m.%Y')
    pvm_loppu = DateField("Loppuu", format='%d.%m.%Y')
    lisaa = SubmitField("Lisää uusi prosessi")

    class Meta:
        csrf = False