# Doctors Endpoints Tests
# Test cases to verify Doctor CRUD api endpoints behaviour
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
def test_doctor_get_all(client, auth_token_name, has_access, invalid_token):
    res = client().get(
        "/api/doctors",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    else:
        if has_access:
            assert res.status_code == 200
            assert isinstance(data["doctors"], list)

    res = client().get(
        "/api/doctors?page=3",
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
def test_doctor_get_single(client, auth_token_name, has_access, invalid_token):
    res = client().get(
        "/api/doctors/1",
        headers={"Authorization": f"Bearer {os.getenv(auth_token_name)}"}
    )
    data = json.loads(res.data)

    if invalid_token:
        assert res.status_code == 401
    else:
        if has_access:
            assert res.status_code == 200
            assert isinstance(data["doctor"], dict)
            assert data["doctor"]["name"] == "Dr. Biswas"

    res = client().get(
        "/api/doctors/100",
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
    ("doctor_bearer_token", False, False),
    ("nurse_bearer_token", False, False),

    # A string with "Bearer" word
    # Eg: Bearer mydummytoken
    ("bad_bearer_token", False, True),

    # An empty string ("")
    ("empty_token", False, True),
])
def test_doctor_create(client, auth_token_name, has_access, invalid_token):
    new_doctor = {"name": "Dr. Sparrow", "age": 42}
    res = client().post(
        "/api/doctors",
        json=new_doctor,
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
        assert data["doctor"]["id"] == 5
        assert data["doctor"]["name"] == "Dr. Sparrow"

    faulty_new_patient = {"name": "Dr. Sparrow"}
    res = client().post(
        "/api/doctors",
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
    ("doctor_bearer_token", False, False),
    ("nurse_bearer_token", False, False),

    # A string with "Bearer" word
    # Eg: Bearer mydummytoken
    ("bad_bearer_token", False, True),

    # An empty string ("")
    ("empty_token", False, True),
])
def test_doctor_update(client, auth_token_name, has_access, invalid_token):
    updated_doctor = {"name": "Dr. Sparrow", "age": 42}
    res = client().patch(
        "/api/doctors/1",
        json=updated_doctor,
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
        assert data["doctor"]["name"] == updated_doctor["name"]
        assert data["doctor"]["age"] == updated_doctor["age"]

    res = client().patch(
        "/api/doctors/100",
        json=updated_doctor,
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


@pytest.mark.parametrize(
    "auth_token_name, has_access, invalid_token, delete_id",
    [
        # General role tokens
        ("dean_bearer_token", True, False, 1),
        ("doctor_bearer_token", False, False, 2),
        ("nurse_bearer_token", False, False, 3),

        # A string with "Bearer" word
        # Eg: Bearer mydummytoken
        ("bad_bearer_token", False, True, 4),

        # An empty string ("")
        ("empty_token", False, True, 5),
    ]
)
def test_doctor_delete(
    client, auth_token_name, has_access, invalid_token, delete_id
):
    res = client().delete(
        f"/api/doctors/{delete_id}",
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
        assert data["doctor_id"] == delete_id

    res = client().delete(
        f"/api/doctors/{delete_id}",
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
