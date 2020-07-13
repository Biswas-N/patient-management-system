from flask import Flask

from .patients import attach_patients_api


def attach_api(app: Flask):
    """
    attach_api(app)
        This function attaches Doctor and Patient CRUD API endpoints to the flask app

    :param app: A Flask instance with database attached
    """
    attach_patients_api(app=app)
