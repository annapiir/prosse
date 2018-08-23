from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.prosessi.models import Prosessi
from application.auth.models import Kayttaja
from application.tehtavat.models import Tehtava
from application.prosessitehtava.models import Prosessitehtava
from application.prosessitehtava.forms import ProsessitehtavaLisaysLomake, ProsessitehtavaMuokkausLomake

from sqlalchemy.sql import text

#Palauttaa prosessinvalintalistan
@app.route("/prosessitehtava/", methods=["GET"])
@login_required
def prosessitehtava_prosessin_valinta():
    return render_template("/prosessitehtava/prosessi.html", prosessit=Prosessi.query.all())

#Hakee näytettävän prosessin
@app.route("/prosessitehtava/", methods=["POST"])
@login_required
def prosessitehtava_lomake():
    prosessi_id = request.form["prosessit"]

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=prosessi_id))

#Palauttaa prosessin tietosivun
@app.route("/prosessitehtava/<prosessi_id>")
@login_required
def prosessitehtava_prosessi_nayta(prosessi_id):

    prosessi = Prosessi.query.get(prosessi_id)
    tehtavat = Prosessitehtava.query.filter_by(prosessi_id=prosessi_id)
    lomakkeet = []

    for tehtava in tehtavat:
        form = ProsessitehtavaMuokkausLomake()
        form.pvm_alku.data = tehtava.pvm_alku
        form.pvm_loppu.data = tehtava.pvm_loppu
        form.aloitettu.data = tehtava.aloitettu
        form.valmis.data = tehtava.valmis
        form.kommentti.data = tehtava.kommentti
        form.id.data = tehtava.id
        form.tehtava_id.data = tehtava.tehtava_id
        form.pvm_kommentti.data = tehtava.pvm_kommentti
        form.kommentoija_id.data = tehtava.kommentoija_id
        lomakkeet.append(form)

    return render_template("/prosessitehtava/list.html", prosessi=prosessi, tehtavat=tehtavat, lomakkeet=lomakkeet)

#Palauttaa prosessitehtävän lisäyslomakkeen
@app.route("/prosessitehtava/uusi/<prosessi_id>/", methods=["GET"])
@login_required
def prosessitehtava_lisays_lomake(prosessi_id):

    prosessi = Prosessi.query.get(prosessi_id)
    tehtavat = Prosessitehtava.query.filter_by(prosessi_id=prosessi_id)
    form = ProsessitehtavaLisaysLomake()

    form.tehtava.choices = [(tehtava.id, tehtava.nimi) for tehtava in Tehtava.query.order_by('id')]

    return render_template("/prosessitehtava/new.html", prosessi=prosessi, tehtavat=tehtavat,
        form=form)

#Lisää uuden prosessitehtävän tietokantaan
@app.route("/prosessitehtava/uusi/<prosessi_id>", methods=["POST"])
@login_required
def prosessitehtava_lisays(prosessi_id):
    form = ProsessitehtavaLisaysLomake(request.form)

    #Muista lisätä validoinnit

    #Jos lomake oli ok, luodaan uusi pt-olio ja viedään kantaan
    pt = Prosessitehtava(prosessi_id, form.tehtava.data, form.pvm_alku.data, form.pvm_loppu.data)

    db.session().add(pt)
    db.session().commit()

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=prosessi_id))

#Tallentaa muokatun tehtävän tiedot kantaan
@app.route("/prosessitehtava/muokkaa/<prosessi_id>/<pt_id>", methods=["POST"])
@login_required
def prosessitehtava_muokkaa(pt_id, prosessi_id):
    form = ProsessitehtavaMuokkausLomake(request.form)

    #Alkuarvot tehtävän aloitukselle ja valmiudelle
    pt = Prosessitehtava.query.get(pt_id)
    orig_aloitettu = pt.aloitettu
    orig_valmis = pt.valmis
    orig_kommentti = pt.kommentti

    #Muokataan prosessitehtävän tietoja
    pt.pvm_alku = form.pvm_alku.data
    pt.pvm_loppu = form.pvm_loppu.data
    pt.aloitettu = form.aloitettu.data
    pt.valmis = form.valmis.data
    pt.kommentti = form.kommentti.data


    #Katsotaan alkuarvojen perusteella, päivitetäänkö kuittaajia 
    if orig_aloitettu == False and pt.aloitettu == True:
        pt.kuittaaja_alku_id = current_user.id

    if orig_valmis == False and pt.valmis == True:
        pt.kuittaaja_alku_id = current_user.id
    
    #Korjaa tämä, nyt on ainakin tyhjänä aina true
    if orig_kommentti != pt.kommentti:
        pt.kommentoija_id = current_user.id
        pt.pvm_kommentti = db.func.current_timestamp()

    print("Alkupäivä:" + str(pt.pvm_alku))
    
    db.session().commit()

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=pt.prosessi_id))