from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.prosessi.models import Prosessi
from application.auth.models import Kayttaja
from application.tehtavat.models import Tehtava
from application.prosessitehtava.models import Prosessitehtava

from sqlalchemy.sql import text

#Lähettää lisätyn prosessin tiedot tietokantaan
#@app.route("/prosessitehtava/<prosessi_id>/", methods=["GET"])
#@login_required
#def prosessitehtava_muokkaa(prosessi_id):
    #form = ProsessiLisaysLomake(request.form)

    #Lomakkeen validointi
    #if not form.validate():
    #    return render_template("prosessi/new.html", form = form)

    #Jos lomake oli ok, muodostetaan uusi tehtäväolio ja viedään kantaan
    #owner_id = current_user.id
    #p = Prosessi(form.prosessin_nimi.data, owner_id, form.pvm_alku.data, form.pvm_loppu.data)

    #db.session().add(p)
    #db.session().commit()
  
   # return redirect(url_for("prosessi_nayta(prosessi_id)"))

#Palauttaa prosessinvalintalistan
@app.route("/prosessitehtava/", methods=["GET"])
def prosessitehtava_prosessin_valinta():
    return render_template("/prosessitehtava/prosessi.html", prosessit=Prosessi.query.all())

#Hakee näytettävän prosessin
@app.route("/prosessitehtava/", methods=["POST"])
def prosessitehtava_lomake():
    prosessi_id = request.form["prosessit"]

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=prosessi_id))

#Palauttaa prosessin tietosivun
@app.route("/prosessitehtava/<prosessi_id>")
def prosessitehtava_prosessi_nayta(prosessi_id):
    prosessi = Prosessi.query.get(prosessi_id)
    tehtavat = Prosessitehtava.query.filter_by(prosessi_id=prosessi_id)
    return render_template("/prosessitehtava/list.html", prosessi=prosessi, tehtavat=tehtavat)
