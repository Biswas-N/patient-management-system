import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

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


class Doctor(db.Model):
    """
    Doctor
    a persistent doctor entity, extends the base SQLAlchemy Model
    """
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    patients = relationship('Patient',
                            backref='doctor',
                            lazy=True,
                            collection_class=list,
                            cascade="save-update, delete")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "patients": self.patients
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.to_json())


class Patient(db.Model):
    """
    Patient
    a persistent patient entity, extends the base SQLAlchemy Model
    """
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    medication = Column(String, default="")
    doctor_id = Column(Integer, ForeignKey('doctors.id'))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "medication": self.medication,
            "doctor_id": self.doctor_id
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.to_json())
