# Patients Endpoints Tests
# Test cases to verify Patient CRUD api endpoints behaviour
# Note: Authentication bearer tokens are pulled from a .env file

import os
import json
import pytest
from dotenv import load_dotenv

from pms import APP, attach_db, get_database_path
from pms.utils import insert_dummy_data


@pytest.fixture(scope="module")
def client():
    load_dotenv()
    attach_db(app=APP, database_path=get_database_path(testing=True))
    insert_dummy_data()

    return APP.test_client


@pytest.mark.parametrize("auth_token_name, has_access, invalid_token", [
    # General role tokens
    ("dean_bearer_token", True, False),
    ("doctor_bearer_token", True, False),
    ("nurse_bearer_token", True, False),

    # A string with "Bearer" word
    # Eg: Bearer mydummytoken
    ("bad_bearer_token", False, True),

    # An empty string ("")
    ("empty_token", False, True),
])
def test_patient_get_all(client, auth_token_name, has_access, invalid_token):
    res = client().get(
        "/api/patients",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    else:
        if has_access:
            assert res.status_code == 200
            assert isinstance(data["patients"], list)

    res = client().get(
        "/api/patients?page=3",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    else:
        if has_access:
            assert res.status_code == 404
            assert data["success"] is False
            assert data["message"] == "resource not found"


@pytest.mark.parametrize("auth_token_name, has_access, invalid_token", [
    # General role tokens
    ("dean_bearer_token", True, False),
    ("doctor_bearer_token", True, False),
    ("nurse_bearer_token", True, False),

    # A string with "Bearer" word
    # Eg: Bearer mydummytoken
    ("bad_bearer_token", False, True),

    # An empty string ("")
    ("empty_token", False, True),
])
def test_patient_get_single(client, auth_token_name, has_access, invalid_token):
    res = client().get(
        "/api/patients/1",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    else:
        if has_access:
            assert res.status_code == 200
            assert isinstance(data["patient"], dict)
            assert data["patient"]["name"] == "Ben 10"

    res = client().get(
        "/api/patients/100",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    else:
        if has_access:
            assert res.status_code == 404
            assert data["success"] is False
            assert data["message"] == "resource not found"


@pytest.mark.parametrize("auth_token_name, has_access, invalid_token", [
    # General role tokens
    ("dean_bearer_token", True, False),
    ("doctor_bearer_token", True, False),
    ("nurse_bearer_token", False, False),

    # A string with "Bearer" word
    # Eg: Bearer mydummytoken
    ("bad_bearer_token", False, True),

    # An empty string ("")
    ("empty_token", False, True),
])
def test_patient_create(client, auth_token_name, has_access, invalid_token):
    new_patient = {"name": "Jack Sparrow", "age": 42, "gender": "Male"}
    res = client().post(
        "/api/patients",
        json=new_patient,
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    elif not has_access:
        assert res.status_code == 403
    else:
        assert res.status_code == 201
        assert data["success"]
        assert data["patient"]["name"] == "Jack Sparrow"
        assert data["patient"]["age"] == 42
        assert data["patient"]["gender"] == "Male"

    faulty_new_patient = {"name": "Jack Sparrow"}
    res = client().post(
        "/api/patients",
        json=faulty_new_patient,
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    elif not has_access:
        assert res.status_code == 403
    else:
        assert res.status_code == 400
        assert data["success"] is False
        assert data["message"] == "bad request"


@pytest.mark.parametrize("auth_token_name, has_access, invalid_token", [
    # General role tokens
    ("dean_bearer_token", True, False),
    ("doctor_bearer_token", True, False),
    ("nurse_bearer_token", False, False),

    # A string with "Bearer" word
    # Eg: Bearer mydummytoken
    ("bad_bearer_token", False, True),

    # An empty string ("")
    ("empty_token", False, True),
])
def test_patient_update(client, auth_token_name, has_access, invalid_token):
    updated_medication = [{"name": "Crosin", "units": "125 ml"},
                          {"name": "Paracetamol", "units": "1 tablet"}]
    res = client().patch(
        "/api/patients/1",
        json=updated_medication,
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    elif not has_access:
        assert res.status_code == 403
    else:
        assert res.status_code == 200
        assert data["success"]
        assert json.loads(data["patient"]["medication"]) == updated_medication

    faulty_updated_medication = [{"name": "Crosin"},
                                 {"units": "1 tablet"}]
    res = client().patch(
        "/api/patients/1",
        json=faulty_updated_medication,
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    elif not has_access:
        assert res.status_code == 403
    else:
        assert res.status_code == 400
        assert data["success"] is False
        assert data["message"] == "bad request"


@pytest.mark.parametrize(
    "auth_token_name, has_access, invalid_token, delete_id",
    [
        # General role tokens
        ("dean_bearer_token", True, False, 1),
        ("doctor_bearer_token", True, False, 2),
        ("nurse_bearer_token", False, False, 3),

        # A string with "Bearer" word
        # Eg: Bearer mydummytoken
        ("bad_bearer_token", False, True, 4),

        # An empty string ("")
        ("empty_token", False, True, 5),
    ]
)
def test_patient_delete(
    client, auth_token_name, has_access, invalid_token, delete_id
):
    res = client().delete(
        f"/api/patients/{delete_id}",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    elif not has_access:
        assert res.status_code == 403
    else:
        assert res.status_code == 200
        assert data["success"]
        assert data["patient_id"] == delete_id

    res = client().delete(
        "/api/patients/100",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    elif not has_access:
        assert res.status_code == 403
    else:
        assert res.status_code == 404
        assert data["success"] is False
        assert data["message"] == "resource not found"
