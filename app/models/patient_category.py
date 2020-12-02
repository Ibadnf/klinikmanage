from app.extensions._db import db


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name_category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name_category
