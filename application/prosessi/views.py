from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.prosessi.models import Prosessi
from application.prosessi.forms import ProsessiMuokkausLomake, ProsessiLisaysLomake
from application.auth.models import Kayttaja

#Palauttaa prosessien listauksen
@app.route("/prosessi/")
def prosessi_lista():
    return render_template("prosessi/list.html", prosessit = Prosessi.query.all()) 

#Palauttaa prosessinmuokkauslomakkeen
@app.route("/prosessi/<prosessi_id>/", methods=["GET"])
@login_required
def prosessi_muokkaa_lomake(prosessi_id):

    #Muodostetaan tehtävä- ja lomakeoliot
    form = ProsessiMuokkausLomake()
    p = Prosessi.query.get(prosessi_id)
    #Annetaan lomakeoliolle prosessin tiedot lähtöarvoiksi
    form.prosessin_nimi.data = p.prosessin_nimi
    form.pvm_alku.data = p.pvm_alku
    form.pvm_loppu.data = p.pvm_loppu

    return render_template("prosessi/edit.html", form=form, prosessi=p)

#Lähettää muokatun prosessin tiedot tietokantaan  
@app.route("/prosessi/<prosessi_id>/", methods=["POST"])
@login_required
def prosessi_muokkaa(prosessi_id):
    form = ProsessiMuokkausLomake(request.form)
    p = Prosessi.query.get(prosessi_id)

    #Haetaan lomakkeelta tiedot
    p.prosessin_nimi = form.prosessin_nimi.data
    p.pvm_alku = form.pvm_alku.data
    p.pvm_loppu = form.pvm_loppu.data

    db.session().commit()
  
    return redirect(url_for("prosessi_lista"))

#Palauttaa prosessinlisäyslomakkeen
@app.route("/prosessi/uusi/")
@login_required
def prosessi_lisays_lomake():
    return render_template("prosessi/new.html", form = ProsessiLisaysLomake())

#Lähettää lisätyn prosessin tiedot tietokantaan
@app.route("/prosessi/", methods=["POST"])
@login_required
def prosessi_lisays():
    form = ProsessiLisaysLomake(request.form)

    #Lomakkeen validointi
    #if not form.validate():
        #return render_template("tehtavat/new.html", form = form)

    #Jos lomake oli ok, muodostetaan uusi tehtäväolio ja viedään kantaan
    owner_id = current_user.id
    p = Prosessi(form.prosessin_nimi.data, owner_id, form.pvm_alku.data, form.pvm_loppu.data)

    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("kayttaja_lista"))