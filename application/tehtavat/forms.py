from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class TehtavaLisaysLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi")
    kuvaus = TextAreaField("Tehtävän kuvaus")

    class Meta:
        csrf = False

class TehtavaMuokkausLomake(FlaskForm):
    kuvaus = TextAreaField("Tehtävän kuvaus")

    class Meta:
        csrf = False