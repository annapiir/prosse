# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
# Käytetään tasks.db-nimistä SQLite-tietokantaa. Kolme vinoviivaa
# kertoo, tiedosto sijaitsee tämän sovelluksen tiedostojen kanssa
# samassa paikassa
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prosse.db"
# Pyydetään SQLAlchemyä tulostamaan kaikki SQL-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tarvittavien tiedostojen sisältö
from application import views

from application.tehtavat import models
from application.tehtavat import views

from application.auth import models
from application.auth import views

from application.prosessi import models
from application.prosessi import views


# kirjautuminen
from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään päästäksesi tähän toiminnallisuuteen."

@login_manager.user_loader
def lataa_kayttaja(user_id):
    return Kayttaja.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut
db.create_all()