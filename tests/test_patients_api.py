# Patients Endpoints Tests
# Test cases to verify Patient CRUD api endpoints behaviour

import json
import pytest

from pms import APP, attach_db, get_database_path
from pms.utils import insert_dummy_data


@pytest.fixture
def client():
    attach_db(app=APP, database_path=get_database_path(testing=True))
    insert_dummy_data()

    return APP.test_client


def test_patient_get_all(client):
    res = client().get("/api/patients")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert isinstance(data["patients"], list)

    res = client().get("/api/patients?page=2")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert isinstance(data["patients"], list)

    res = client().get("/api/patients?page=3")
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"


def test_patient_get_single(client):
    res = client().get("/api/patients/1")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert isinstance(data["patient"], dict)
    assert data["patient"]["name"] == "Ben 10"

    res = client().get("/api/patients/100")
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"


def test_patient_create(client):
    new_patient = {"name": "Jack Sparrow", "age": 42, "gender": "Male"}
    res = client().post("/api/patients", json=new_patient)
    data = json.loads(res.data)

    assert res.status_code == 201
    assert data["success"]
    assert data["patient"]["id"] == 13
    assert data["patient"]["name"] == "Jack Sparrow"

    faulty_new_patient = {"name": "Jack Sparrow"}
    res = client().post("/api/patients", json=faulty_new_patient)
    data = json.loads(res.data)

    assert res.status_code == 400
    assert data["success"] is False
    assert data["message"] == "bad request"


def test_patient_update(client):
    updated_medication = [{"name": "Crosin", "units": "125 ml"},
                          {"name": "Paracetamol", "units": "1 tablet"}]
    res = client().patch("/api/patients/1", json=updated_medication)
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data["success"]
    assert json.loads(data["patient"]["medication"]) == updated_medication

    faulty_updated_medication = [{"name": "Crosin"},
                                 {"units": "1 tablet"}]
    res = client().patch("/api/patients/1", json=faulty_updated_medication)
    data = json.loads(res.data)

    assert res.status_code == 400
    assert data["success"] is False
    assert data["message"] == "bad request"


def test_patient_delete(client):
    res = client().delete("/api/patients/1")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data["success"]
    assert data["patient_id"] == 1

    res = client().delete("/api/patients/100")
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"
