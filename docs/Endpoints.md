# Endpoints

## Overview

These are the following endpoints available to access Patients and Doctors resources in Patient Management System application

1. Patients CRUD API (start with `/api`)
    | Endpoint  | Purpose  | Access Roles |
    |-----------|----------|-------------|
    |GET `/patients?page=<page_no>`|Get all patients (10 per page)|Nurse, Doctor and Dean|
    |GET `/patients/<int:id>`|Get single patient by ID|Nurse, Doctor and Dean|
    |POST `/patients`|Create a new patient|Doctor and Dean|
    |PATCH `/patients/<int:id>`|Update a patient's medication|Doctor and Dean|
    |DELETE `/patients/<int:id>`|Delete a patient| Doctor and Dean|

2. Doctors CRUD API (start with `/api`)
    | Endpoint  | Purpose  | Access Roles |
    |-----------|----------|-------------|
    |GET `/doctors?page=<page_no>`|Get all doctors (10 per page)|Nurse, Doctor and Dean|
    |GET `/doctors/<int:id>`|Get single doctor by ID|Nurse, Doctor and Dean|
    |POST `/doctors`|Create a new doctor|Dean|
    |PATCH `/doctors/<int:id>`|Update a doctor's name and/or age|Dean|
    |DELETE `/doctors/<int:id>`|Delete a doctor|Dean|

3. Endpoints handled by frontend (React)
    | Endpoint  | Purpose  | Authenticated User |
    |-----------|----------|--------------------|
    |`/`|Includes login information|NO|
    |`/callback`|Stores bearer token and auto redirects to `/`|YES|
    |`/patients`|Displays list of patients (Makes a request to `/api/patients`)|YES|
    |`/patients/<int:id>`|Displays a single patient (Makes a request to `/api/patients/<id>`)|YES|
    |`/doctors`|Displays list of doctors (Makes a request to `/api/doctors`)|YES|
    |`/doctors/<int:id>`|Displays a single patient (Makes a request to `/api/doctors/<id>`)|YES|

## Detailed Information

### Patients CRUD API

#### `GET /patients?page=<page_no>`
Returns a JSON object holding total_patients (count), patients (as a list), success (boolean) and last_page (boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    RESPONSE BODY:
        {
            "last_page": false,
            "patients": [
                {
                    "doctor_name": "Dr. Biswas",
                    "id": 1,
                    "name": "Ben 10"
                },
                {
                    "doctor_name": "Dr. Biswas",
                    "id": 2,
                    "name": "Gwen Stacy"
                },
                {
                    "doctor_name": "Dr. Reed Richards",
                    "id": 3,
                    "name": "Barry Allen"
                }
            ],
            "success": true,
            "total_patients": 3
        }
    ```

#### `GET /patients/<int:patient_id>`
Returns a JSON object holding the patient (JSON object) and success(boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    RESPONSE BODY:
        {
            "patient": {
                "age": 10,
                "doctor": {
                    "id": 1,
                    "name": "Dr. Biswas",
                    "patients_count": 4
                },
                "gender": "Male",
                "id": 1,
                "medication": "[{"name": "Crosin", "units": "125 ml"}]",
                "name": "Ben 10"
            },
            "success": true
        }
    ```

#### `POST /patients`
Creates a new patient record and returns a JSON object holding the new patient data (JSON object) and success (boolean)

> STATUS CODES: 200, 400, 401, 403

EXCEPTIONS:
- TypeError (400 - when request body has wrong data or wrong data structure)
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)

    ```
    REQUEST BODY:
        {
            "name": "Ben 10",
            "age": 10,
            "gender": "Male"
        }

    RESPONSE BODY:
        {
            "patient": {
                "age": 10,
                "doctor": null,
                "gender": "Male",
                "id": 12,
                "medication": "",
                "name": "Ben 10"
            },
            "success": true
        }
    ```

#### `PATCH /patients/<int:patient_id>`
Updates the medication in an existing patient record and returns a JSON object with updated patient data and success (boolean)

> STATUS CODES: 200,400, 401, 403, 404

EXCEPTIONS:
- TypeError (400 - when request body has wrong data or data structure)
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    REQUEST BODY:
        [
            {
                "name": "Crosin",
                "units": "125 ml"
            },
            {
                "name": "Paracetemol",
                "units": "2x tablets"
            }
        ]

    RESPONSE BODY:
        {
            "patient": {
                "age": 10,
                "doctor": {
                    "id": 1,
                    "name": "Dr. Biswas",
                    "patients_count": 4
                },
                "gender": "Male",
                "id": 1,
                "medication": "[{\"name\": \"Crosin\", \"units\": \"125 ml\"}, {\"name\": \"Paracetemol\", \"units\": \"2x tablets\"}]",
                "name": "Ben 10"
            },
            "success": true
        }
    ```

#### ` DELETE /patients/<int:patient_id>`
Deletes an existing patient record and returns a JSON object with deleted patient id and success (boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    RESPONSE BODY:
        {
            "patient_id": 11,
            "success": true
        }
    ```

### Doctors CRUD API

#### `GET /doctors?page=<page_no>`
Returns a JSON object holding total_doctors (count), doctors (as a list), success (boolean) and last_page (boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    RESPONSE BODY:
        {
            "doctors": [
                {
                    "id": 1,
                    "name": "Dr. Biswas",
                    "patients_count": 4
                },
                {
                    "id": 2,
                    "name": "Dr. Batman",
                    "patients_count": 0
                }
            ],
            "last_page": true,
            "success": true,
            "total_doctors": 2
        }
    ```

#### `GET /doctors/<int:doctor_id>`
Returns a JSON object holding the doctor (JSON object) and success(boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    RESPONSE BODY:
        {
            "doctor": {
                "age": 25,
                "id": 1,
                "name": "Dr. Biswas",
                "patients": [
                    {
                        "doctor_name": "Dr. Biswas",
                        "id": 1,
                        "name": "Ben 10"
                    },
                    {
                        "doctor_name": "Dr. Biswas",
                        "id": 2,
                        "name": "Gwen Stacy"
                    }
                ]
            },
            "success": true
        }
    ```

#### `POST /doctors`
Creates a new doctor record and returns a JSON object holding the new doctor data (JSON object) and success (boolean)

> STATUS CODES: 200, 400, 401, 403

EXCEPTIONS:
- TypeError (400 - when request body has wrong data or wrong data structure)
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)

    ```
    REQUEST BODY:
        {
            "name": "Dr. Ben Tennison",
            "age": 30
        }

    RESPONSE BODY:
        {
            "doctor": {
                "age": 30,
                "id": 5,
                "name": "Dr. Ben Tennison",
                "patients": []
            },
            "success": true
        }
    ```

#### `PATCH /doctors/<int:doctor_id>`
Updates the name or/and age of a doctor, if the key exists in the incoming request body

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    REQUEST BODY:
        {
            "name": "Dr. Ben Tennison",
            "age": 24
        }

    RESPONSE BODY:
        {
            "doctor": {
                "age": 24,
                "id": 5,
                "name": "Dr. Ben Tennison",
                "patients": []
            },
            "success": true
        }
    ```

#### ` DELETE /doctors/<int:doctor_id>`
Deletes an existing doctor record and returns a JSON object with deleted doctor id and success (boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    RESPONSE BODY:
        {
            "doctor_id": 5,
            "success": true
        }
    ```