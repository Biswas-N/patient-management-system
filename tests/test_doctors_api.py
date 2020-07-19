# Doctors Endpoints Tests
# Test cases to verify Doctor CRUD api endpoints behaviour

import json
import pytest

from pms import APP, attach_db, get_database_path
from pms.utils import insert_dummy_data


@pytest.fixture
def client():
    attach_db(app=APP, database_path=get_database_path(testing=True))
    insert_dummy_data()

    return APP.test_client


def test_doctor_get_all(client):
    res = client().get("/api/doctors")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert isinstance(data["doctors"], list)

    res = client().get("/api/doctors?page=3")
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"


def test_doctor_get_single(client):
    res = client().get("/api/doctors/1")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert isinstance(data["doctor"], dict)
    assert data["doctor"]["name"] == "Dr. Biswas"

    res = client().get("/api/doctors/100")
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"


def test_doctor_create(client):
    new_doctor = {"name": "Dr. Sparrow", "age": 42}
    res = client().post("/api/doctors", json=new_doctor)
    data = json.loads(res.data)

    assert res.status_code == 201
    assert data["success"]
    assert data["doctor"]["id"] == 5
    assert data["doctor"]["name"] == "Dr. Sparrow"

    faulty_new_patient = {"name": "Dr. Sparrow"}
    res = client().post("/api/doctors", json=faulty_new_patient)
    data = json.loads(res.data)

    assert res.status_code == 400
    assert data["success"] is False
    assert data["message"] == "bad request"


def test_doctor_update(client):
    updated_doctor = {"name": "Dr. Sparrow", "age": 42}
    res = client().patch("/api/doctors/1", json=updated_doctor)
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data["success"]
    assert data["doctor"]["name"] == updated_doctor["name"]
    assert data["doctor"]["age"] == updated_doctor["age"]

    res = client().patch("/api/doctors/100", json=updated_doctor)
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"


def test_doctor_delete(client):
    res = client().delete("/api/doctors/1")
    data = json.loads(res.data)

    assert res.status_code == 200
    assert data["success"]
    assert data["doctor_id"] == 1

    res = client().delete("/api/doctors/100")
    data = json.loads(res.data)

    assert res.status_code == 404
    assert data["success"] is False
    assert data["message"] == "resource not found"
