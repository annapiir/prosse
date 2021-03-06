from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import Kayttaja
from application.auth.forms import KirjautuminenLomake, KayttajaMuokkausLomake, KayttajaLisaysLomake


#Kirjautuminen
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = KirjautuminenLomake())

    form = KirjautuminenLomake(request.form)

    kayttaja = Kayttaja.query.filter_by(tunnus=form.tunnus.data, salasana=form.salasana.data).first()
    
    if not kayttaja:
        return render_template("auth/login.html", form = form,
                               error = "Käyttäjätunnusta tai salasanaa ei löydy")

    login_user(kayttaja)
    return redirect(url_for("index")) 


#Uloskirjautuminen
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   


#Käyttäjien listaus
@app.route("/auth/users")
@login_required(role="ADMIN")
def kayttaja_lista():
    return render_template("auth/list.html", kayttajat = Kayttaja.query.all()) 


#Käyttäjän tietojen muokkauslomake
@app.route("/auth/<kayttaja_id>/", methods=["GET"])
@login_required(role="ADMIN")
def kayttaja_muokkaa_lomake(kayttaja_id):

    form = KayttajaMuokkausLomake()
    kayttaja = Kayttaja.query.get(kayttaja_id)

    form.tunnus.data = kayttaja.tunnus
    form.kayttajan_nimi.data = kayttaja.kayttajan_nimi
    form.salasana.data = kayttaja.salasana

    return render_template("auth/edit.html", form=form, kayttaja=kayttaja)


#Lähettää muokatun käyttäjän tiedot tietokantaan  
@app.route("/auth/<kayttaja_id>/", methods=["POST"])
@login_required(role="ADMIN")
def kayttaja_muokkaa(kayttaja_id):
    form = KayttajaMuokkausLomake(request.form)
    k = Kayttaja.query.get(kayttaja_id)

    if not form.validate():
        return render_template("auth/edit.html", form = form)

    k.kayttajan_nimi = form.kayttajan_nimi.data
    k.tunnus = form.tunnus.data
    k.salasana = form.salasana.data

    db.session().commit()
  
    return redirect(url_for("kayttaja_lista"))


#Palauttaa käyttäjänlisäyslomakkeen
@app.route("/auth/uusi/")
def kayttaja_lisays_lomake():
    return render_template("auth/new.html", form = KayttajaLisaysLomake())


#Lähettää lisätyn käyttäjän tiedot tietokantaan
@app.route("/auth/", methods=["POST"])
def kayttaja_lisays():
    form = KayttajaLisaysLomake(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    k = Kayttaja(form.kayttajan_nimi.data, form.tunnus.data, form.salasana.data)

    db.session().add(k)
    db.session().commit()
  
    return redirect(url_for("kayttaja_lista"))