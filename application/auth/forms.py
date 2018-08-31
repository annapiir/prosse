from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators
  
class KirjautuminenLomake(FlaskForm):
    tunnus = StringField("Käyttäjätunnus")
    salasana = PasswordField("Salasana")
        
  
    class Meta:
        csrf = False

class KayttajaMuokkausLomake(FlaskForm):
    tunnus = StringField("Käyttäjätunnus",
        [validators.InputRequired("Anna käyttäjätunnus"),
        validators.Length(max=8, message="Käyttäjätunnus saa olla korkeintaan 8 merkkiä")])
    kayttajan_nimi = StringField("Nimi",
        [validators.Length(min=2, message="Nimen pitää olla vähintään kaksi merkkiä")])
    salasana = PasswordField("Salasana",
        [validators.Length(min=5, message="Salasanan pitää olla vähintään 5 merkkiä"),
        validators.Length(max=144, message="Salasana voi olla korkeintaan 144 merkkiä")])
    tallenna = SubmitField("Tallenna")

    class Meta:
        csrf = False

class KayttajaLisaysLomake(FlaskForm):
    tunnus = StringField("Käyttäjätunnus", 
        [validators.InputRequired("Anna käyttäjätunnus"),
        validators.Length(max=8, message="Käyttäjätunnus saa olla korkeintaan 8 merkkiä")])
    kayttajan_nimi = StringField("Nimi",
        [validators.Length(min=2, message="Nimen pitää olla vähintään kaksi merkkiä")])
    salasana = PasswordField("Salasana", 
        [validators.Length(min=5, message="Salasanan pitää olla vähintään 5 merkkiä"),
        validators.Length(max=144, message="Salasana voi olla korkeintaan 144 merkkiä")])
    lisaa = SubmitField("Lisää uusi käyttäjä")

    class Meta:
            csrf = False