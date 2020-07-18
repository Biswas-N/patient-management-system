from flask import Flask, request, abort, jsonify

from pms.models import Doctor
from pms.auth import requires_auth

ITEMS_PER_PAGE = 10
BASE_URL = "api"


def attach_doctors_api(app: Flask):
    """
    attach_doctors_api(app)
        This function attaches Doctor CRUD API endpoints to the flask app

    @Input app: A Flask instance with database attached
    """

    @app.route(f"/{BASE_URL}/doctors")
    @requires_auth("read:doctor")
    def doctors_get_all():
        """
        GET /doctors handler
            Returns a JSON object holding total_doctors (count), doctors
            (as a list) and success (boolean)

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

        doctors = Doctor.query.all()
        formatted_doctors = [doctor.to_json() for doctor in doctors]

        # Response case 1:
        #   If no doctors record in the database,
        #   then reply with an empty list and count of zero
        if page_number == 1 and len(formatted_doctors) == 0:
            return jsonify({
                "success": True,
                "total_doctors": 0,
                "doctors": formatted_doctors
            })
        # Response case 2:
        #   If doctors record in the database,
        #   then reply with a json formatted doctors list and number of
        #   doctors
        elif page_number > 0 and start < len(formatted_doctors):
            return jsonify({
                "success": True,
                "total_doctors": len(formatted_doctors),
                "doctors": formatted_doctors[start:end]
            })
        # Response case 3:
        #   If invalid case (like trying to access page outside limit),
        #   then reply with 404
        else:
            abort(404)

    @app.route(f"/{BASE_URL}/doctors/<int:doctor_id>")
    @requires_auth("read:doctor")
    def doctor_get_single(doctor_id):
        """
        GET /doctors/<int:doctor_id> handler
            Returns a JSON object holding the doctor (JSON object) and
            success(boolean)

            STATUS CODES: 200, 401, 403, 404
            EXCEPTIONS: - ResourceNotFound (404 - when tried to access
                            unknown or non existing doctor)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        doctor = Doctor.query.get_or_404(doctor_id)

        return jsonify({
            "success": True,
            "doctor": doctor.to_json()
        })

    @app.route(f"/{BASE_URL}/doctors", methods=["POST"])
    @requires_auth("create:doctor")
    def doctor_create():
        """
        POST /doctors handler
            Creates a new doctor record and returns a JSON object holding
            the new doctor data (JSON object) and success (boolean)

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
            # Raises TypeError, when data does not include keys "name"
            # and "age" (These two fields are non nullable)
            new_doctor = Doctor(**data)
            new_doctor.insert()

            return jsonify({
                "success": True,
                "doctor": new_doctor.to_json()
            }), 201
        except TypeError:
            abort(400)

    @app.route(f"/{BASE_URL}/doctors/<int:doctor_id>", methods=["PATCH"])
    @requires_auth("update:doctor")
    def doctor_update(doctor_id):
        """
        PATCH /doctors/<int:doctor_id>"
            Updates the name or/and age of a doctor, if the key exists in the
            incoming request body

            STATUS CODES: 200, 401, 403, 404
            EXCEPTIONS: - ResourceNotFound (404 - when tried to update unknown
                            or non existing doctor)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        data = request.get_json()

        doctor = Doctor.query.get_or_404(doctor_id)

        if "name" in data:
            doctor.name = data["name"]
            doctor.update()

        if "age" in data:
            doctor.age = data["age"]

        return {
            "success": True,
            "doctor": doctor.to_json()
        }

    @app.route(f"/{BASE_URL}/doctors/<int:doctor_id>", methods=["DELETE"])
    @requires_auth("delete:doctor")
    def doctor_delete(doctor_id):
        """
        DELETE /doctors/<int:doctor_id> handler
            Deletes an existing doctor record and returns a JSON object with
            deleted doctor id and success (boolean)

            STATUS CODES: 200, 401, 403, 404
            EXCEPTIONS: - ResourceNotFound (404 - when tried to delete unknown
                            or non existing doctor)
                        - AuthenticationError (401 - when bearer token not
                            found or found but incorrect)
                        - AuthorizationError (403 - when user does not have
                            the required permissions to access the endpoint)
        """
        doctor = Doctor.query.get_or_404(doctor_id)
        doctor_id_copy = doctor.id
        doctor.delete()

        return jsonify({
            "success": True,
            "doctor_id": doctor_id_copy
        })
