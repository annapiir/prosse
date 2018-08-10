from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField
  

class ProsessiMuokkausLomake(FlaskForm):
    prosessin_nimi = StringField("Prosessin nimi")
    pvm_alku = DateField("Alkaa")
    pvm_loppu = DateField("Loppuu")
    tallenna = SubmitField("Tallenna")

    class Meta:
        csrf = False

class ProsessiLisaysLomake(FlaskForm):
    prosessin_nimi = StringField("Prosessin nimi")
    pvm_alku = DateField("Alkaa")
    pvm_loppu = DateField("Loppuu")
    lisaa = SubmitField("Lisää uusi prosessi")

    class Meta:
        csrf = False