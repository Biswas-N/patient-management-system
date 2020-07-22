import pytest

from pms import APP
from pms.models import Doctor, attach_db, Patient
from pms.utils import insert_dummy_data, get_database_path


@pytest.fixture()
def setup():
    attach_db(app=APP, database_path=get_database_path(testing=True))
    insert_dummy_data()


def test_doctor_get_all(setup):
    all_doctors = Doctor.query.all()
    assert len(all_doctors) == 4


def test_doctor_get_single(setup):
    # For existing entity
    single_doctor = Doctor.query.filter(Doctor.name == "Dr. Biswas").first()
    assert single_doctor.age == 25

    # For non - existing entity
    single_doctor = Doctor.query.filter(Doctor.name == "Non Existing").first()
    assert single_doctor is None


def test_doctor_create(setup):
    sample_doctor_data = {"name": "Dr. Tony Stark", "age": 45}
    sample_doctor = Doctor(**sample_doctor_data)
    sample_doctor.insert()

    assert sample_doctor.id == 5


def test_doctor_update(setup):
    doctor = Doctor.query.filter(Doctor.name == "Dr. Biswas").first()
    doctor.age = doctor.age - 2
    doctor.update()

    assert doctor.id == 1
    assert doctor.name == "Dr. Biswas"
    assert doctor.age == 23


def test_doctor_delete(setup):
    doctor = Doctor.query.filter(Doctor.name == "Dr. Biswas").first()
    doctor_id_copy = doctor.id
    doctor.delete()

    doctor = Doctor.query.get(doctor_id_copy)

    assert doctor is None


def test_patient_get_all(setup):
    all_patients = Patient.query.all()
    assert len(all_patients) == 12


def test_patient_get_single(setup):
    # For existing entity
    single_patient = Patient.query.filter(Patient.name == "Gwen Stacy").first()
    assert single_patient.age == 20

    # For non - existing entity
    single_patient = Patient.query.filter(Patient.name == "Non Existing").first()
    assert single_patient is None


def test_patient_create(setup):
    sample_patient_data = {"name": "Oliver Queen", "age": 32, "gender": "Male"}
    sample_patient = Patient(**sample_patient_data)
    sample_patient.insert()

    assert sample_patient.id == 13


def test_patient_update(setup):
    patient = Patient.query.filter(Patient.name == "Ben 10").first()
    patient.age = patient.age + 2
    patient.update()

    assert patient.id == 1
    assert patient.name == "Ben 10"
    assert patient.age == 12


def test_patient_delete(setup):
    patient = Patient.query.filter(Patient.name == "Ben 10").first()
    patient_id_copy = patient.id
    patient.delete()

    patient = Patient.query.get(patient_id_copy)

    assert patient is None
