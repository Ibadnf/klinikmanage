from app.extensions._db import db


class PemberiObatModel(db.Model):
    __tablename__ = 'pemberi_obat'

    id_obat = db.Column(db.Integer, primary_key=True)
    no_opname = db.Column(db.String(64), unique=True, nullable=False)
    id_rekam = db.Column(db.Integer, db.ForeignKey('rekam_medis.id_rekam'), nullable=False)
    id_patient = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    keterangan = db.Column(db.String(512), nullable=False)
    tgl_tindakan = db.Column(db.DateTime, nullable=False)
    data_obat = db.Column(db.String(512), nullable=False)
    kode_obat = db.Column(db.String(64), nullable=False)
    jumlah_obat = db.Column(db.String(64), nullable=False)
    

    def __repr(self):
        return f"<pemberi_obat {self.kode_obat}>"
