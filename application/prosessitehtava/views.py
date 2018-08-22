from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.prosessi.models import Prosessi
from application.auth.models import Kayttaja
from application.tehtavat.models import Tehtava
from application.prosessitehtava.models import Prosessitehtava
from application.prosessitehtava.forms import ProsessitehtavaLisaysLomake

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

#Palauttaa prosessitehtävän lisäyslomakkeen
@app.route("/prosessitehtava/uusi/<prosessi_id>/", methods=["GET"])
def prosessitehtava_lisays_lomake(prosessi_id):

    prosessi = Prosessi.query.get(prosessi_id)
    tehtavat = Prosessitehtava.query.filter_by(prosessi_id=prosessi_id)
    form = ProsessitehtavaLisaysLomake()

    form.tehtava.choices = [(tehtava.id, tehtava.nimi) for tehtava in Tehtava.query.order_by('id')]

    return render_template("/prosessitehtava/new.html", prosessi=prosessi, tehtavat=tehtavat,
        form=form)

#Lisää uuden prosessitehtävän tietokantaan
@app.route("/prosessitehtava/uusi/<prosessi_id>", methods=["POST"])
def prosessitehtava_lisays(prosessi_id):
    form = ProsessitehtavaLisaysLomake(request.form)

    #Muista lisätä validoinnit

    #Jos lomake oli ok, luodaan uusi pt-olio ja viedään kantaan
    pt = Prosessitehtava(prosessi_id, form.tehtava.data, form.pvm_alku.data, form.pvm_loppu.data)

    db.session().add(pt)
    db.session().commit()

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=prosessi_id))

#Tallentaa muokatun tehtävän tiedot kantaan
@app.route("/prosessitehtava/muokkaa/<prosessi_id>", methods=["POST"])
def prosessitehtava_muokkaa(pt_id, prosessi_id):

    pt = Prosessitehtava.query.get(pt_id)

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=pt.prosessi_id))