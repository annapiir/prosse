from flask import render_template
from application import app
from application.auth.models import Kayttaja

@app.route("/")
def index():
    return render_template("index.html", prosessit_lkm=Kayttaja.montako_prosessia_kayttajalla(),
    prosessit=Kayttaja.kayttajan_prosessit(), 
    tehtavat_lkm=Kayttaja.kayttajan_keskeneraiset_tehtavat_lkm())

