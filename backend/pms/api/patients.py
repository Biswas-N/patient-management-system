import json
from flask import Flask, request, abort, jsonify

from backend.pms.models import Patient

ITEMS_PER_PAGE = 10


def attach_patients_api(app: Flask):
    """
    attach_patients_api(app)
        This function attaches Patient CRUD API endpoints to the flask app

    :param app: A Flask instance with database attached
    """
    @app.route("/patients")
    def get_all_patients():
        page_number = request.args.get("page", 1, type=int)
        start = ITEMS_PER_PAGE * (page_number - 1)
        end = start + ITEMS_PER_PAGE

        patients = Patient.query.all()
        formatted_patients = [patient.to_json() for patient in patients]

        if page_number == 1 and len(formatted_patients) == 0:
            return jsonify({
                "success": True,
                "total_patients": 0,
                "patients": formatted_patients
            })
        elif page_number > 0 and start < len(formatted_patients):
            return jsonify({
                "success": True,
                "total_patients": len(formatted_patients),
                "patients": formatted_patients[start:end]
            })
        else:
            abort(404)

    @app.route("/patients/<int:patient_id>")
    def get_single_patient(patient_id):
        patient = Patient.query.get_or_404(patient_id)

        return jsonify({
            "success": True,
            "patient": patient.to_json()
        })

    @app.route("/patients", methods=["POST"])
    def create_patient():
        data = request.get_json()

        try:
            new_patient = Patient(**data)
            new_patient.insert()

            return jsonify({
                "success": True,
                "patient": new_patient.to_json()
            }), 201
        except TypeError:
            abort(400)

    @app.route("/patients/<int:patient_id>", methods=["PATCH"])
    def update_patient(patient_id):
        data = request.get_json()

        patient = Patient.query.get_or_404(patient_id)

        if set([("name" in medication and "units" in medication) for medication in data]) == {True}:
            patient.medication = json.dumps(data)
            patient.update()

            return {
                "success": True,
                "patient": patient.to_json()
            }
        else:
            abort(400)

    @app.route("/patients/<int:patient_id>", methods=["DELETE"])
    def delete_patient(patient_id):
        patient = Patient.query.get_or_404(patient_id)
        patient_id_copy = patient.id
        patient.delete()

        return jsonify({
            "success": True,
            "patient_id": patient_id_copy
        })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
