# Tuodaan Flask käyttöön
from flask import Flask
app = Flask(__name__)

# Tuodaan SQLAlchemy käyttöön
from flask_sqlalchemy import SQLAlchemy
import os
#Jos ympäristö on Heroku
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
#Jos ympäristö on paikallinen
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prosse.db"    
    app.config["SQLALCHEMY_ECHO"] = True

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)


# kirjautuminen
from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
from flask_login import current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään päästäksesi tähän toiminnallisuuteen."

# roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated():
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Luetaan kansiosta application tarvittavien tiedostojen sisältö
from application import views

from application.tehtavat import models
from application.tehtavat import views

from application.auth import models
from application.auth import views

from application.prosessi import models
from application.prosessi import views

from application.prosessitehtava import models
from application.prosessitehtava import views


@login_manager.user_loader
def lataa_kayttaja(user_id):
    return Kayttaja.query.get(user_id)

# Luodaan lopulta tarvittavat tietokantataulut, mutta vain jos niitä ei ole ennestään
try: 
    db.create_all()
except:
    pass