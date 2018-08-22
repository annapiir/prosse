from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField, validators, SelectField, BooleanField
  

class ProsessitehtavaLisaysLomake(FlaskForm):
    tehtava = SelectField('Tehtävä')
    pvm_alku = DateField("Alkaa", format='%d.%m.%Y')
    pvm_loppu = DateField("Päättyy", format='%d.%m.%Y')
    #To do: Lisää validointi päivämäärille
    tallenna = SubmitField("Tallenna")
    

    class Meta:
        csrf = False