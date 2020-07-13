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
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"},
                       {"name": "Ben 10", "age": 10, "gender": "Male"},
                       {"name": "Gwen Stacy", "age": 20, "gender": "Female"},
                       {"name": "Barry Allen", "age": 23, "gender": "Male"},
                       {"name": "Arthur Curry", "age": 52, "gender": "Male"},
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"},
                       {"name": "Arthur Curry", "age": 52, "gender": "Male"},
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"}]

    for patient in sample_patients:
        temp_patient = Patient(name=patient["name"], age=patient["age"], gender=patient["gender"])
        random_doctor = random.choice(sample_doctors)
        temp_patient.doctor = Doctor.query.filter(Doctor.name == random_doctor["name"]).first()

        temp_patient.insert()


class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = APP
        attach_db(app=self.app, database_path=get_database_path(testing=True))
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

    def test_doctor_create(self):
        sample_doctor_data = {"name": "Dr. Tony Stark", "age": 45}
        sample_doctor = Doctor(**sample_doctor_data)
        sample_doctor.insert()

        self.assertEqual(5, sample_doctor.id)

    def test_doctor_update(self):
        doctor = Doctor.query.filter(Doctor.name == "Dr. Biswas").first()
        doctor.age = doctor.age - 2
        doctor.update()

        self.assertEqual(1, doctor.id)
        self.assertEqual("Dr. Biswas", doctor.name)
        self.assertEqual(23, doctor.age)

    def test_doctor_delete(self):
        doctor = Doctor.query.filter(Doctor.name == "Dr. Biswas").first()
        doctor_id_copy = doctor.id
        doctor.delete()

        doctor = Doctor.query.get(doctor_id_copy)

        self.assertIsNone(doctor)

    def test_patient_get_all(self):
        all_patients = Patient.query.all()
        self.assertEqual(12, len(all_patients))

    def test_patient_get_single(self):
        # For existing entity
        single_patient = Patient.query.filter(Patient.name == "Gwen Stacy").first()
        self.assertTrue(20, single_patient.age)

        # For non - existing entity
        single_patient = Patient.query.filter(Patient.name == "Non Existing").first()
        self.assertIsNone(single_patient)

    def test_patient_create(self):
        sample_patient_data = {"name": "Oliver Queen", "age": 32, "gender": "Male"}
        sample_patient = Patient(**sample_patient_data)
        sample_patient.insert()

        self.assertEqual(13, sample_patient.id)

    def test_patient_update(self):
        patient = Patient.query.filter(Patient.name == "Ben 10").first()
        patient.age = patient.age + 2
        patient.update()

        self.assertEqual(1, patient.id)
        self.assertEqual("Ben 10", patient.name)
        self.assertEqual(12, patient.age)

    def test_patient_delete(self):
        patient = Patient.query.filter(Patient.name == "Ben 10").first()
        patient_id_copy = patient.id
        patient.delete()

        patient = Patient.query.get(patient_id_copy)

        self.assertIsNone(patient)


if __name__ == '__main__':
    unittest.main()
