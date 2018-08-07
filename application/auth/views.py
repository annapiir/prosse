from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import Kayttaja
from application.auth.forms import KirjautuminenLomake

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = KirjautuminenLomake())

    form = KirjautuminenLomake(request.form)
    # mahdolliset validoinnit

    kayttaja = Kayttaja.query.filter_by(tunnus=form.tunnus.data, salasana=form.salasana.data).first()
    
    if not kayttaja:
        return render_template("auth/login.html", form = form,
                               error = "Käyttäjätunnusta tai salasanaa ei löydy")


    login_user(kayttaja)
    return redirect(url_for("index")) 

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    
