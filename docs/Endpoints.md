# Endpoints

## Overview

These are the following endpoints available to access Patients and Doctors resources in Patient Management System application

> *Note: All endpoints included below start with "/api"*

1. Patients related endpoints

    | Endpoint  | Purpose  | Access Roles |
    |-----------|----------|-------------|
    |GET `/patients?page=<page_no>`|Get all patients (10 per page)|Nurse, Doctor and Dean|
    |GET `/patients/<int:id>`|Get single patient by ID|Nurse, Doctor and Dean|
    |POST `/patients`|Create a new patient|Doctor and Dean|
    |PATCH `/patients/<int:id>`|Update a patient's medication|Doctor and Dean|
    |DELETE `/patients/<int:id>`|Delete a patient| Doctor and Dean|

2. Doctors related endpoints
    | Endpoint  | Purpose  | Access Roles |
    |-----------|----------|-------------|
    |GET `/doctors?page=<page_no>`|Get all doctors (10 per page)|Nurse, Doctor and Dean|
    |GET `/doctors/<int:id>`|Get single doctor by ID|Nurse, Doctor and Dean|
    |POST `/doctors`|Create a new doctor|Dean|
    |PATCH `/doctors/<int:id>`|Update a doctor's name and/or age|Dean|
    |DELETE `/doctors/<int:id>`|Delete a doctor|Dean|


## Detailed Information

### `GET '/patients?page=<page_no>'`
Returns a JSON object holding total_patients (count), patients
(as a list), success (boolean) and last_page (boolean)

> STATUS CODES: 200, 401, 403, 404

EXCEPTIONS:
- AuthenticationError (401 - when bearer token not found or found but incorrect)
- AuthorizationError (403 - when user does not have the required permissions to access the endpoint)
- ResourceNotFound (404 - when tried to access pages exceeding the limit)

    ```       
    EXAMPLE:
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
            "total_patients": 10
        }
    ```