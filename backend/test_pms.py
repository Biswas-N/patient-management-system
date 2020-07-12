import unittest
import random

from backend.pms import APP, attach_db, get_database_path
from backend.pms.models import db, Doctor, Patient


def insert_dummy_data() -> None:
    db.drop_all()
    db.create_all()

    sample_doctors = [{"name": "Dr. Biswas", "age": 25},
                      {"name": "Dr. Batman", "age": 42},
                      {"name": "Dr. Who", "age": 125},
                      {"name": "Dr. Reed Richards", "age": 42}]

    for doctor in sample_doctors:
        temp_doctor = Doctor(name=doctor["name"], age=doctor["age"])
        temp_doctor.insert()

    sample_patients = [{"name": "Ben 10", "age": 10, "gender": "Male"},
                       {"name": "Gwen Stacy", "age": 20, "gender": "Female"},
                       {"name": "Barry Allen", "age": 23, "gender": "Male"},
                       {"name": "Arthur Curry", "age": 52, "gender": "Male"},
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"}]

    for patient in sample_patients:
        temp_patient = Patient(name=patient["name"], age=patient["age"], gender=patient["gender"])
        random_doctor = random.choice(sample_doctors)
        temp_patient.doctor = Doctor.query.filter(Doctor.name == random_doctor["name"]).first()

        temp_patient.insert()


class ModelsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = APP
        attach_db(app=self.app, database_path=get_database_path())
        self.client = self.app.test_client

        insert_dummy_data()

    def test_doctor_get_all(self):
        all_doctors = Doctor.query.all()
        self.assertEqual(4, len(all_doctors))

    def test_doctor_get_single(self):
        # For existing entity
        single_doctor = Doctor.query.filter(Doctor.name == "Dr. Biswas").first()
        self.assertTrue(25, single_doctor.age)

        # For non - existing entity
        single_doctor = Doctor.query.filter(Doctor.name == "Non Existing").first()
        self.assertIsNone(single_doctor)

    def test_patient_get_all(self):
        all_patients = Patient.query.all()
        self.assertEqual(5, len(all_patients))

    def test_patient_get_single(self):
        # For existing entity
        single_patient = Patient.query.filter(Patient.name == "Gwen Stacy").first()
        self.assertTrue(20, single_patient.age)

        # For non - existing entity
        single_patient = Patient.query.filter(Patient.name == "Non Existing").first()
        self.assertIsNone(single_patient)


if __name__ == '__main__':
    unittest.main()
