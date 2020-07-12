import unittest

from backend.pms import APP, attach_db, get_database_path
from backend.pms.models import db, Doctor


def insert_dummy_data() -> None:
    db.drop_all()
    db.create_all()

    sample_doctors = [{"name": "Biswas", "age": 25},
                      {"name": "Batman", "age": 42},
                      {"name": "Dr Who", "age": 125}]

    for doctor in sample_doctors:
        temp_doctor = Doctor(name=doctor["name"], age=doctor["age"])
        temp_doctor.insert()

    # sample_patients = []


class ModelsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = APP
        attach_db(app=self.app, database_path=get_database_path())
        self.client = self.app.test_client

        insert_dummy_data()

    def test_doctor_get_all(self):
        all_doctors = Doctor.query.all()
        self.assertEqual(3, len(all_doctors))

    def test_doctor_get_single(self):
        # For existing entity
        single_doctor = Doctor.query.filter(Doctor.name == "Biswas").first()
        self.assertTrue(25, single_doctor.age)

        # For non - existing entity
        single_doctor = Doctor.query.filter(Doctor.name == "Non Existing").first()
        self.assertIsNone(single_doctor)


if __name__ == '__main__':
    unittest.main()
