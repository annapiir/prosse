from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

class TehtavaLisaysLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi" 
        ,[validators.Length(min=2, message="Nimen pitää olla vähintään kaksi merkkiä pitkä"), 
        validators.Length(max=144, message="Nimi saa olla korkeintaan 144 merkkiä")])
    kuvaus = TextAreaField("Tehtävän kuvaus"
        ,[validators.Length(max=300, message="Kuvaus saa olla korkeintaan 300 merkkiä")])
    lisaa = SubmitField("Lisää uusi tehtävä")

    class Meta:
        csrf = False

class TehtavaMuokkausLomake(FlaskForm):
    kuvaus = TextAreaField("Tehtävän kuvaus",
        [validators.Length(max=300, message="Kuvaus saa olla korkeintaan 300 merkkiä")])
    tallenna = SubmitField("Tallenna")
    poista = SubmitField("Poista")

    class Meta:
        csrf = False