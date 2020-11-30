from app.extensions._db import db


class InsuranceModel(db.Model):
    __tablename__ = 'insurances'

    id = db.Column(db.Integer, primary_key=True)
    insurance_name = db.Column(db.String(50), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id_patient'), nullable=False)

    def __repr__(self):
        return '<Insurance %r>' % self.insurance_name
