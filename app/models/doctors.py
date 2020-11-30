from app.extensions._db import db


class DoctorsModel(db.Model):
    __tablename__ = 'doctors'

    id_dokter = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    full_name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(512),nullable=False)
    hp = db.Column(db.String(128), nullable=False)
    alamat = db.Column(db.String(512),nullable=False)


    def __repr(self):
        return f"<Doctors {self.full_name}>"
