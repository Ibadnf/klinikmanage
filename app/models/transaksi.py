from app.extensions._db import db


class TransaksiModel(db.Model):
    __tablename__ = 'transaksi'

    id_transaksi = db.Column(db.Integer, primary_key=True)
    id_patient = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    id_insurance = db.Column(db.Integer, db.ForeignKey('insurances.id'), nullable=False)
    cost = db.Column(db.Integer, nullable=False)

    def __repr(self):
        return f"<Transaksi {self.id_patient}>"
