from app.extensions._db import db

class PatientsModel(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(128), nullable=False)
    no_ktp = db.Column(db.String(64), unique=True, nullable=False)
    tempat_lahir = db.Column(db.String(64), nullable=False)
    tgl_lahir = db.Column(db.Date, nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    alamat = db.Column(db.String(512), nullable=False)
    pekerjaan = db.Column(db.String(64), nullable=False)
    hp = db.Column(db.String(15), nullable=False)
    rekam_medis = db.relationship('RekamMedisModel', backref='patients', lazy=True)
    transaction = db.relationship('TransaksiModel', backref='patients', lazy=True)
    agama = db.Column(db.String(15), nullable=False)
    pendidikan = db.Column(db.String(15), nullable=False)
    obat = db.relationship('PemberiObatModel', backref='patients', lazy=True)

    def __repr(self):
        return f"<Patients {self.full_name}>"
