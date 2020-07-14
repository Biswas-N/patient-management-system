import unittest
import json

from backend.pms import APP, attach_db, get_database_path
from backend.pms.models import Doctor, Patient
from backend.pms.utils import insert_dummy_data


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


class PatientEndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = APP
        attach_db(app=self.app, database_path=get_database_path(testing=True))
        self.client = self.app.test_client

        insert_dummy_data()

    def test_patient_get_all(self):
        res = self.client().get("/patients")
        data = json.loads(res.data)

        self.assertEqual(200, res.status_code)
        self.assertTrue(isinstance(data["patients"], list))

        res = self.client().get("/patients?page=2")
        data = json.loads(res.data)

        self.assertEqual(200, res.status_code)
        self.assertTrue(isinstance(data["patients"], list))

        res = self.client().get("/patients?page=3")
        data = json.loads(res.data)

        self.assertEqual(404, res.status_code)
        self.assertFalse(data["success"])
        self.assertEqual("resource not found", data["message"])

    def test_patient_get_single(self):
        res = self.client().get("/patients/1")
        data = json.loads(res.data)

        self.assertEqual(200, res.status_code)
        self.assertTrue(isinstance(data["patient"], dict))
        self.assertEqual("Ben 10", data["patient"]["name"])

        res = self.client().get("/patients/100")
        data = json.loads(res.data)

        self.assertEqual(404, res.status_code)
        self.assertFalse(data["success"])
        self.assertEqual("resource not found", data["message"])

    def test_patient_create(self):
        new_patient = {"name": "Jack Sparrow", "age": 42, "gender": "Male"}
        res = self.client().post("/patients", json=new_patient)
        data = json.loads(res.data)

        self.assertEqual(201, res.status_code)
        self.assertTrue(data["success"])
        self.assertTrue(data["patient"]["id"])
        self.assertEqual("Jack Sparrow", data["patient"]["name"])

        faulty_new_patient = {"name": "Jack Sparrow"}
        res = self.client().post("/patients", json=faulty_new_patient)
        data = json.loads(res.data)

        self.assertEqual(400, res.status_code)
        self.assertFalse(data["success"])
        self.assertEqual("bad request", data["message"])

    def test_patient_update(self):
        updated_medication = [{"name": "Crosin", "units": "125 ml"},
                              {"name": "Paracetamol", "units": "1 tablet"}]
        res = self.client().patch("/patients/1", json=updated_medication)
        data = json.loads(res.data)

        self.assertEqual(200, res.status_code)
        self.assertTrue(data["success"])
        self.assertEqual(updated_medication, json.loads(data["patient"]["medication"]))

        faulty_updated_medication = [{"name": "Crosin"},
                                     {"units": "1 tablet"}]
        res = self.client().patch("/patients/1", json=faulty_updated_medication)
        data = json.loads(res.data)

        self.assertEqual(400, res.status_code)
        self.assertFalse(data["success"])
        self.assertEqual("bad request", data["message"])

    def test_patient_delete(self):
        res = self.client().delete("/patients/1")
        data = json.loads(res.data)

        self.assertEqual(200, res.status_code)
        self.assertTrue(data["success"])
        self.assertEqual(1, data["patient_id"])

        res = self.client().delete("/patients/100")
        data = json.loads(res.data)

        self.assertEqual(404, res.status_code)
        self.assertFalse(data["success"])
        self.assertEqual("resource not found", data["message"])


if __name__ == '__main__':
    unittest.main()
