from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, validators, SelectField, BooleanField, IntegerField
  

class ProsessitehtavaLisaysLomake(FlaskForm):
    tehtava = SelectField("Tehtävä")
    pvm_alku = DateField("Alkaa", format='%d.%m.%Y')
    pvm_loppu = DateField("Päättyy", format='%d.%m.%Y')
    tekija = SelectField("Tekijä")
    #To do: Lisää validointi päivämäärille
    tallenna = SubmitField("Tallenna")
    
    class Meta:
        csrf = False

class ProsessitehtavaMuokkausLomake(FlaskForm):
    id = IntegerField("Prosessitehtävän ID")
    tehtava_id = IntegerField("Tehtävän ID")
    tehtava_nimi = StringField("Tehtävän nimi")
    pvm_alku = DateField("Alkaa", format='%d.%m.%Y')
    pvm_loppu = DateField("Päättyy", format='%d.%m.%Y')
    aloitettu = BooleanField("Aloitettu")
    valmis = BooleanField("Valmis")
    #To do: Lisää validointi, ettei samaa tekijää voi lisätä kahdesti
    tekija = SelectField("Tekijä")
    nykyiset_tekijat = SelectField("Nykyiset tekijät")
    kommentti = StringField("Kommentti")
    kommentoija_id = IntegerField("Kommentoija")
    kommentoija_tunnus = StringField("Kommentoijan nimi")
    pvm_kommentti = DateField("Pvm")
    #To do: Lisää validointi päivämäärille
    tallenna = SubmitField("Tallenna")
    
    class Meta:
        csrf = False