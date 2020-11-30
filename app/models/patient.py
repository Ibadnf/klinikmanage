from app.extensions._db import db

class PatientsModel(db.Model):
    __tablename__ = 'patients'

    id_patient = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    full_name = db.Column(db.String(128), nullable=False)
    no_ktp = db.Column(db.String(64), nullable=False)
    ttl = db.Column(db.Date, nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    alamat = db.Column(db.String(512), nullable=False)
    pekerjaan = db.Column(db.String(64), nullable=False)
    hp = db.Column(db.String(15), nullable=False)
    kategori = db.relationship('CategoryModel', backref='patient', lazy=True)
    asuransi = db.relationship('InsuranceModel', backref='patient', lazy=True)
    agama = db.Column(db.String(15), nullable=False)
    pendidikan = db.Column(db.String(15), nullable=False)

    def __repr(self):
        return f"<Patients {self.full_name}>"
