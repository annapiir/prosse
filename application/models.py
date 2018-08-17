from application import db

class Base(db.Model):

    __abstract__ = True
  
    id = db.Column(db.Integer, primary_key=True)
    pvm_luonti = db.Column(db.DateTime, default=db.func.current_timestamp())
    pvm_muokkaus = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())