
from app import create_app
from app.extensions._db import db
from app.models.users import UsersModel
from app.models.doctors import DoctorsModel
from app.models.patient import PatientsModel
from app.models.patient_insurance import InsuranceModel
from app.models.patient_category import CategoryModel

app = create_app()


def migrate_all():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        migrate_all()