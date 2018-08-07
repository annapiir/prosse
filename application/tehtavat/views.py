from application import app, db
from flask import redirect, render_template, request, url_for
from application.tehtavat.models import Tehtava
from application.tehtavat.forms import TehtavaLisaysLomake, TehtavaMuokkausLomake

#Palauttaa listan tehtävistä
@app.route("/tehtavat", methods=["GET"])
def tehtavat_lista():
    return render_template("tehtavat/list.html", tehtavat = Tehtava.query.all())

#Palauttaa tehtävänlisäyslomakkeen
@app.route("/tehtavat/uusi/")
def tehtavat_lomake():
    return render_template("tehtavat/new.html", form = TehtavaLisaysLomake())

#Palattaa muokattavaksi valitun tehtävän tiedot lomakkeella 
@app.route("/tehtavat/<tehtava_id>/", methods=["GET"])
def tehtavat_muokkaa_lomake(tehtava_id):

    #Muodostetaan tehtävä- ja lomakeoliot
    form = TehtavaMuokkausLomake()
    tehtava = Tehtava.query.get(tehtava_id)
    #Annetaan lomakeolion kuvaukselle tehtävän kuvaus lähtöarvoksi
    form.kuvaus.data = tehtava.kuvaus

    return render_template("tehtavat/edit.html", form=form, tehtava=tehtava)

#Lähettää muokatun tehtävän tiedot tietokantaan  
@app.route("/tehtavat/<tehtava_id>/", methods=["POST"])
def tehtavat_muokkaa(tehtava_id):
    form = TehtavaMuokkausLomake(request.form)
    t = Tehtava.query.get(tehtava_id)
    t.kuvaus = form.kuvaus.data
    db.session().commit()
  
    return redirect(url_for("tehtavat_lista"))

#Lähettää lisätyn tehtävän tiedot tietokantaan
@app.route("/tehtavat/", methods=["POST"])
def tehtavat_luo():
    form = TehtavaLisaysLomake(request.form)

    #Lomakkeen validointi
    if not form.validate():
        return render_template("tehtavat/new.html", form = form)

    #Jos lomake oli ok, muodostetaan uusi tehtäväolio ja viedään kantaan
    t = Tehtava(form.nimi.data, form.kuvaus.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tehtavat_lista"))