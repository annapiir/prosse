from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.tehtavat.models import Tehtava
from application.tehtavat.forms import TehtavaLisaysLomake, TehtavaMuokkausLomake


#Palauttaa listan tehtävistä
@app.route("/tehtavat", methods=["GET"])
def tehtavat_lista():
    return render_template("tehtavat/list.html", tehtavat = Tehtava.query.all())


#Palauttaa tehtävänlisäyslomakkeen
@app.route("/tehtavat/uusi/", methods=["GET"])
@login_required
def tehtavat_lomake():
    return render_template("tehtavat/new.html", form = TehtavaLisaysLomake())


#Palauttaa valitun tehtävän tiedot lomakkeella
@app.route("/tehtavat/<tehtava_id>/", methods=["GET"])
def tehtavat_nayta(tehtava_id):
    return render_template("tehtavat/tehtava.html", tehtava=Tehtava.query.get(tehtava_id))


#Palattaa muokattavaksi valitun tehtävän tiedot lomakkeella 
@app.route("/tehtavat/muokkaa/<tehtava_id>/", methods=["GET"])
@login_required
def tehtavat_muokkaa_lomake(tehtava_id):

    form = TehtavaMuokkausLomake()
    tehtava = Tehtava.query.get(tehtava_id)

    form.kuvaus.data = tehtava.kuvaus

    return render_template("tehtavat/edit.html", form=form, tehtava=tehtava)

#Lähettää muokatun tehtävän tiedot tietokantaan  
@app.route("/tehtavat/muokkaa/<tehtava_id>/", methods=["POST"])
@login_required
def tehtavat_muokkaa(tehtava_id):
    form = TehtavaMuokkausLomake(request.form)
    t = Tehtava.query.get(tehtava_id)

    if not form.validate():
        return render_template("tehtavat/edit.html", form = form)

    if form.validate_on_submit():
        if form.tallenna.data:
            t.kuvaus = form.kuvaus.data
            db.session().commit()
        elif form.poista.data:
            db.session().delete(t)
            db.session().commit()

    return redirect(url_for("tehtavat_lista"))

#Lähettää lisätyn tehtävän tiedot tietokantaan
@app.route("/tehtavat/", methods=["POST"])
@login_required
def tehtavat_luo():
    form = TehtavaLisaysLomake(request.form)

    if not form.validate():
        return render_template("tehtavat/new.html", form = form)

    t = Tehtava(form.nimi.data, form.kuvaus.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tehtavat_lista"))

#Poistaa tehtävän  
@app.route("/tehtavat/<tehtava_id>/", methods=["POST"])
@login_required
def tehtavat_poista(tehtava_id):
    t = Tehtava.query.get(tehtava_id)

    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("tehtavat_lista"))