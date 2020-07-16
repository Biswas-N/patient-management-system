from flask import Flask, jsonify

from .patients import attach_patients_api
from .doctors import attach_doctors_api


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
