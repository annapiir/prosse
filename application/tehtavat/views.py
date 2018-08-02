from application import app, db
from flask import redirect, render_template, request, url_for
from application.tehtavat.models import Tehtava

#Palauttaa listan tehtävistä
@app.route("/tehtavat", methods=["GET"])
def tehtavat_lista():
    return render_template("tehtavat/list.html", tehtavat = Tehtava.query.all())

#Palauttaa tehtävänlisäyslomakkeen
@app.route("/tehtavat/uusi/")
def tehtavat_lomake():
    return render_template("tehtavat/new.html")

#Palattaa muokattavaksi valitun tehtävän tiedot lomakkeella 
@app.route("/tehtavat/<tehtava_id>/", methods=["GET"])
def tehtavat_muokkaa_lomake(tehtava_id):
    return render_template("tehtavat/edit.html", tehtava = Tehtava.query.get(tehtava_id))

#Lähettää muokatun tehtävän tiedot tietokantaan  
@app.route("/tehtavat/<tehtava_id>/", methods=["POST"])
def tehtavat_muokkaa(tehtava_id):

    t = Tehtava.query.get(tehtava_id)
    t.kuvaus = request.form.get("kuvaus")
    db.session().commit()
  
    return redirect(url_for("tehtavat_lista"))

#Lähettää lisätyn tehtävän tiedot tietokantaan
@app.route("/tehtavat/", methods=["POST"])
def tehtavat_luo():
    t = Tehtava(request.form.get("nimi"), request.form.get("kuvaus"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tehtavat_lista"))