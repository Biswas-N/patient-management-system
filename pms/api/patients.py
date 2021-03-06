import json
from flask import Flask, request, abort, jsonify

from pms.models import Patient
from pms.auth import requires_auth

ITEMS_PER_PAGE = 10
BASE_URL = "api"


def attach_patients_api(app: Flask):
    """
    attach_patients_api(app)
        This function attaches Patient CRUD API endpoints to the flask app

    app: A Flask instance with database attached
    """

    @app.route(f"/{BASE_URL}/patients")
    @requires_auth("read:patient")
    def patient_get_all(payload):
        """
        GET /patients handler
            Returns a JSON object holding total_patients (count), patients
            (as a list), success (boolean) and last_page (boolean)

            STATUS CODES: 200, 401, 403, 404
            EXCEPTIONS: - ResourceNotFound (404 - when tried to access pages
                            exceeding the limit)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        page_number = request.args.get("page", 1, type=int)
        start = ITEMS_PER_PAGE * (page_number - 1)
        end = start + ITEMS_PER_PAGE

        patients = Patient.query.all()
        formatted_patients = [patient.short() for patient in patients]

        last_page = True if (end > len(formatted_patients)) else False

        # Response case 1:
        #   If no patients record in the database,
        #   then reply with an empty list and count of zero
        if page_number == 1 and len(formatted_patients) == 0:
            return jsonify({
                "success": True,
                "total_patients": 0,
                "patients": formatted_patients,
                "last_page": last_page
            })
        # Response case 2:
        #   If patients record in the database,
        #   then reply with a json formatted patients list and number of
        #   patients
        elif page_number > 0 and start < len(formatted_patients):
            return jsonify({
                "success": True,
                "total_patients": len(formatted_patients),
                "patients": formatted_patients[start:end],
                "last_page": last_page
            })
        # Response case 3:
        #   If invalid case (like trying to access page outside limit),
        #   then reply with 404
        else:
            abort(404)

    @app.route(f"/{BASE_URL}/patients/<int:patient_id>")
    @requires_auth("read:patient")
    def patient_get_single(payload, patient_id):
        """
        GET /patients/<int:patient_id> handler
            Returns a JSON object holding the patient (JSON object) and
            success(boolean)

            STATUS CODES: 200, 401, 403, 404
            EXCEPTIONS: - ResourceNotFound (404 - when tried to access
                            unknown or non existing patient)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        patient = Patient.query.get_or_404(patient_id)

        return jsonify({
            "success": True,
            "patient": patient.long()
        })

    @app.route(f"/{BASE_URL}/patients", methods=["POST"])
    @requires_auth("create:patient")
    def patient_create(payload):
        """
        POST /patients handler
            Creates a new patient record and returns a JSON object holding
            the new patient data (JSON object) and success (boolean)

            STATUS CODES: 200, 400, 401, 403
            EXCEPTIONS: - TypeError (400 - when request body has wrong data
                            or data structure)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        data = request.get_json()

        try:
            # Raises TypeError, when data does not include keys "name",
            # "age" and "gender" (These three fields are non nullable)
            new_patient = Patient(**data)
            new_patient.insert()

            return jsonify({
                "success": True,
                "patient": new_patient.long()
            }), 201
        except TypeError:
            abort(400)

    @app.route(f"/{BASE_URL}/patients/<int:patient_id>", methods=["PATCH"])
    @requires_auth("update:patient")
    def patient_update(payload, patient_id):
        """
        PATCH /patients/<int:patient_id> handler
            Updates the medication in an existing patient record and returns
            a JSON object with updated patient data and success (boolean)

            STATUS CODES: 200, 400, 401, 403, 404
            EXCEPTIONS: - TypeError (400 - when request body has wrong data
                            or data structure)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
                        - ResourceNotFound (404 - when tried to update unknown
                            or non existing patient)
        """
        data = request.get_json()

        patient = Patient.query.get_or_404(patient_id)

        if set(
            [(
                "name" in medication and "units" in medication
            ) for medication in data]
        ) == {True}:
            patient.medication = json.dumps(data)
            patient.update()

            return {
                "success": True,
                "patient": patient.long()
            }
        else:
            abort(400)

    @app.route(f"/{BASE_URL}/patients/<int:patient_id>", methods=["DELETE"])
    @requires_auth("delete:patient")
    def patient_delete(payload, patient_id):
        """
        DELETE /patients/<int:patient_id> handler
            Deletes an existing patient record and returns a JSON object with
            deleted patient id and success (boolean)

            STATUS CODES: 200, 401, 403, 404
            EXCEPTIONS: - ResourceNotFound (404 - when tried to delete unknown
                            or non existing patient)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        patient = Patient.query.get_or_404(patient_id)
        patient_id_copy = patient.id
        patient.delete()

        return jsonify({
            "success": True,
            "patient_id": patient_id_copy
        })
