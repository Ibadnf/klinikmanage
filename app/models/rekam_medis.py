from app.extensions._db import db


class RekamMedisModel(db.Model):
    __tablename__ = 'rekam_medis'

    id_rekam = db.Column(db.Integer, primary_key=True)
    id_patient = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    no_rekam = db.Column(db.String(64), unique=True, nullable=False)
    no_register = db.Column(db.String(128), nullable=False)
    keluarga = db.Column(db.String(64),nullable=False)
    hp_keluarga = db.Column(db.String(24), nullable=False)
    tgl_masuk = db.Column(db.DateTime, nullable=False)
    tgl_keluar = db.Column(db.DateTime, nullable=False)
    room = db.Column(db.String(16), nullable=False)
    keluhan = db.Column(db.String(512), nullable=False)
    riwayat_penyakit = db.Column(db.String(512), nullable=False)
    alergi_obat = db.Column(db.String(512),nullable=False)
    apoteker = transaction = db.relationship('PemberiObatModel', backref='rekam_medis', lazy=True)

    def __repr(self):
        return f"<rekam_medis {self.no_rekam}>"
