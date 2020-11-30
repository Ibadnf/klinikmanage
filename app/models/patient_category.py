from app.extensions._db import db


class CategoryModel(db.Model):
    __tablename__ = 'patients_category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id_patient'), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name
