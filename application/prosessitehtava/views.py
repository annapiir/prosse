from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.prosessi.models import Prosessi
from application.auth.models import Kayttaja
from application.tehtavat.models import Tehtava
from application.prosessitehtava.models import Prosessitehtava, Tekija
from application.prosessitehtava.forms import ProsessitehtavaLisaysLomake, ProsessitehtavaMuokkausLomake

from sqlalchemy.sql import text, func


#Palauttaa prosessinvalintalistan
@app.route("/prosessitehtava/", methods=["GET"])
@login_required
def prosessitehtava_prosessin_valinta():
    return render_template("/prosessitehtava/prosessi.html", prosessit=Prosessi.query.all())


#Palauttaa prosessin tietosivun
@app.route("/prosessitehtava/<prosessi_id>")
@login_required
def prosessitehtava_prosessi_nayta(prosessi_id):

    prosessi = Prosessi.query.get(prosessi_id)
    omistaja = Kayttaja.query.get(prosessi.owner_id)
    omistaja_tunnus = omistaja.kayttaja_tunnus()
    tehtavat = Prosessitehtava.query.filter_by(prosessi_id=prosessi_id)
    lomakkeet = []

    #Haetaan tehtäväkohtaisille lomakkeille tiedot 
    for tehtava in tehtavat:
        t = Tehtava.query.get(tehtava.tehtava_id)

        hae_tekijat = text("SELECT Kayttaja.id, Kayttaja.tunnus FROM Kayttaja"
                    " JOIN Tekija on Kayttaja.id = Tekija.tekija_id"
                    " WHERE Tekija.pt_id = :tehtava_id").params(tehtava_id = tehtava.id)
        tekijat = db.engine.execute(hae_tekijat)

        hae_uudet_tekijat = text("SELECT Kayttaja.id, Kayttaja.tunnus FROM Kayttaja"
                    " WHERE Kayttaja.id NOT IN" 
                    " (SELECT Tekija.tekija_id FROM Tekija WHERE Tekija.pt_id = :tehtava_id)").params(tehtava_id = tehtava.id)

        lista = db.engine.execute(hae_uudet_tekijat)
        uudet_tekijat = []
        for tekija in lista:
            uudet_tekijat.append([tekija.id, tekija.tunnus])

        print(uudet_tekijat)

        if tehtava.kommentoija_id:
            k = Kayttaja.query.get(tehtava.kommentoija_id)
        else:
            k = None

        form = ProsessitehtavaMuokkausLomake()

        if tehtava.pvm_alku:
            form.pvm_alku.data = tehtava.pvm_alku.date()
        else:
            form.pvm_alku.data = None

        if tehtava.pvm_loppu:
            form.pvm_loppu.data = tehtava.pvm_loppu.date()
        else:
            form.pvm_loppu.data = None

        form.aloitettu.data = tehtava.aloitettu
        form.valmis.data = tehtava.valmis
        form.kommentti.data = tehtava.kommentti
        form.id.data = tehtava.id
        form.tehtava_id.data = tehtava.tehtava_id
        form.tehtava_nimi.data = t.tehtavan_nimi()
        form.pvm_kommentti.data = tehtava.pvm_kommentti
        form.kommentoija_id.data = tehtava.kommentoija_id
        form.tekija.choices = uudet_tekijat
        form.tekija.choices.insert(0, (0, "Lisää uusi"))
        form.nykyiset_tekijat.choices = tekijat

        if k != None:
            form.kommentoija_tunnus.data = k.kayttaja_tunnus()
        else:
            form.kommentoija_tunnus.data = None

        lomakkeet.append(form)

    lomakkeet.sort(key=lambda lomake: lomake['pvm_alku'].data)

    return render_template("/prosessitehtava/list.html", prosessi=prosessi, tehtavat=tehtavat, 
    lomakkeet=lomakkeet, omistaja_tunnus=omistaja_tunnus)


#Hakee näytettävän prosessin
@app.route("/prosessitehtava/", methods=["POST"])
@login_required
def prosessitehtava_lomake():
    prosessi_id = request.form["prosessit"]

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=prosessi_id))


#Palauttaa prosessitehtävän lisäyslomakkeen
@app.route("/prosessitehtava/uusi/<prosessi_id>/", methods=["GET"])
@login_required
def prosessitehtava_lisays_lomake(prosessi_id):

    prosessi = Prosessi.query.get(prosessi_id)
    tehtavat = Prosessitehtava.query.filter_by(prosessi_id=prosessi_id)
    form = ProsessitehtavaLisaysLomake()

    form.tekija.choices = [(tekija.id, tekija.tunnus) for tekija in Kayttaja.query.all()]
    form.tehtava.choices = [(tehtava.id, tehtava.nimi) for tehtava in Tehtava.query.order_by('id')]

    return render_template("/prosessitehtava/new.html", prosessi=prosessi, tehtavat=tehtavat,
        form=form)


#Lisää uuden prosessitehtävän tietokantaan
@app.route("/prosessitehtava/uusi/<prosessi_id>", methods=["POST"])
@login_required
def prosessitehtava_lisays(prosessi_id):
    form = ProsessitehtavaLisaysLomake(request.form)

    pt = Prosessitehtava(prosessi_id, form.tehtava.data, form.pvm_alku.data, form.pvm_loppu.data)
    db.session().add(pt)
    db.session().commit()

    pt_id = db.session.query(func.max(Prosessitehtava.id)).scalar()
    tekija = Tekija(pt_id, int(form.tekija.data))
    db.session().add(tekija)
    db.session().commit()
 
    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=prosessi_id))


#Tallentaa muokatun tehtävän tiedot kantaan
@app.route("/prosessitehtava/muokkaa/<prosessi_id>/<pt_id>", methods=["POST"])
@login_required
def prosessitehtava_muokkaa(pt_id, prosessi_id):
    form = ProsessitehtavaMuokkausLomake(request.form)

    #Alkuarvot, joihin verrataan päivitystarvetta
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
    
    #Bugi: Päivittää tyhjän kommentin aina
    if orig_kommentti != pt.kommentti:
        pt.kommentoija_id = current_user.id
        pt.pvm_kommentti = db.func.current_timestamp()

    if Kayttaja.query.get(form.tekija.data):
        tekija = Tekija(pt_id, int(form.tekija.data))
        db.session.add(tekija)
    
    db.session().commit()

    return redirect(url_for("prosessitehtava_prosessi_nayta", prosessi_id=pt.prosessi_id))