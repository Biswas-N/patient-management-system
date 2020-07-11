from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def attach_db(app: Flask, database_path: str):
    """
    attach_db binds a database to a flask application
    using SQLAlchemy library
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
