from flask import Flask, jsonify

from pms.api.patients import attach_patients_api
from pms.api.doctors import attach_doctors_api
from pms.auth import AuthError


def attach_api(app: Flask):
    """
    attach_api(app)
        This function attaches Doctor and Patient CRUD API endpoints to the flask app

    app: A Flask instance with database attached
    """
    attach_patients_api(app=app)
    attach_doctors_api(app=app)
    attach_errorhandlers(app=app)


def attach_errorhandlers(app: Flask):
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

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            "success": False,
            "code": error.error['code'],
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code
