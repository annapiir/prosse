from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
  
class KirjautuminenLomake(FlaskForm):
    tunnus = StringField("Käyttäjätunnus")
    salasana = PasswordField("Salasana")
  
    class Meta:
        csrf = False

class KayttajaMuokkausLomake(FlaskForm):
    tunnus = StringField("Käyttäjätunnus")
    kayttajan_nimi = StringField("Nimi")
    salasana = PasswordField("Salasana")
    tallenna = SubmitField("Tallenna")

    class Meta:
        csrf = False

class KayttajaLisaysLomake(FlaskForm):
    tunnus = StringField("Käyttäjätunnus")
    kayttajan_nimi = StringField("Nimi")
    salasana = PasswordField("Salasana")
    lisaa = SubmitField("Lisää uusi käyttäjä")