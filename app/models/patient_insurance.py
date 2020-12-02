from app.extensions._db import db


class InsuranceModel(db.Model):
    __tablename__ = 'insurances'

    id = db.Column(db.Integer, primary_key=True)
    name_insurance = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Insurance %r>' % self.insurance_name
