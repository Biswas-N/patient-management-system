from flask import Flask

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
