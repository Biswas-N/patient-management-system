import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


def attach_db(app: Flask, database_path: str):
    """
    attach_db
        binds a database to a flask application using SQLAlchemy library
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

    # Auto incrementing, unique primary key
    id = Column(Integer, primary_key=True)  # Eg: 130
    name = Column(String, nullable=False)  # Eg: "Biswas"
    age = Column(Integer, nullable=False)  # Eg: 25
    # SQLAlchemy ORM relationship
    # This relationship enables accessing the patient and doctor data
    # bi-directionally
    patients = relationship('Patient',
                            backref='doctor',
                            lazy=True,
                            collection_class=list,
                            cascade="save-update, delete")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def short(self):
        """
        short(self)
            Method to return short representation of the doctor object

            EXAMPLE:
                {
                    "id": 21,
                    "name": "Dr. Biswas",
                    "patients_count": 3
                }
        """
        return {
            "id": self.id,
            "name": self.name,
            "patients_count": len(self.patients)
        }

    def long(self):
        """
        long(self)
            Method to return long representation of a doctor object

            EXAMPLE:
                {
                    "id": 21,
                    "name": "Dr. Biswas",
                    "age": 25,
                    "patients": [
                        {
                            "id": 2,
                            "name": "Peter Parker",
                            "age": 21,
                            "doctor_name": "Dr. Biswas"
                        }
                    ]
                }
        """
        formatted_patients = [patient.short() for patient in self.patients]
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "patients": formatted_patients
        }

    def insert(self):
        """
        insert(self)
            inserts a new doctor into the database

            EXAMPLE
                doctor = Doctor(name="Dr. Biswas", age=25)
                doctor.insert()
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        delete(self)
            deletes a doctor from the database

            EXAMPLE
                doctor = Doctor
                            .query
                            .filter(Doctor.name == "Dr. Biswas")
                            .first()
                doctor.delete()
        """
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """
        update(self)
            updates an existing doctor information in the database

            EXAMPLE
                doctor = Doctor
                            .query
                            .filter(Doctor.name == "Dr. Biswas")
                            .first()
                doctor.age = doctor.age + 1
                doctor.update()
        """
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.to_json())


class Patient(db.Model):
    """
    Patient
        a persistent patient entity, extends the base SQLAlchemy Model
    """
    __tablename__ = "patients"

    # Auto incrementing, unique primary key
    id = Column(Integer, primary_key=True)  # Eg: 130
    name = Column(String, nullable=False)  # Eg: "Dr. Batman"
    age = Column(Integer, nullable=False)  # Eg: 32
    # Gender can be a Enum (planning to implement in future)
    # Right now restrictions to the data inputted are implemented
    # using frontend and endpoints code
    gender = Column(String, nullable=False)  # Eg: Male / Female
    # Medication is a lazy json blob
    # Sample data type - [{"name" : string, "units" : string}]
    # Eg: [{"name": "Crosin", "units": "125 ml"}]
    medication = Column(String, default="")
    # Automatically filled when a doctor is assigned to a patient
    # Eg: sample_patient.doctor = sample_doctor
    doctor_id = Column(Integer, ForeignKey('doctors.id'))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def short(self):
        """
        short(self)
            Method to return short representation of the Patient object

            EXAMPLE:
                {
                    "id": 2,
                    "name": "Peter Parker",
                    "age": 21,
                    "doctor_name": "Dr. Biswas"
                }
        """
        formatted_doctor = self.doctor.name if self.doctor else None
        return {
            "id": self.id,
            "name": self.name,
            "doctor_name": formatted_doctor
        }

    def long(self):
        """
        long(self)
            Method to return long representation of the Patient instance

            EXAMPLE:
                {
                    "id": 2,
                    "name": "Peter Parker",
                    "age": 21,
                    "gender": "Male",
                    "medication": [{"name": "Crosin", "units": "125 ml"},
                                  {"name": "Paracetemal", "units": "2 tablets"}],
                    "doctor": {
                        "id": 21,
                        "name": "Dr. Biswas",
                        "patients_count": 3
                    }
                }
        """
        formatted_doctor = self.doctor.short() if self.doctor else None
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "medication": self.medication,
            "doctor": formatted_doctor
        }

    def insert(self):
        """
        insert(self)
            inserts a new patient into the database

            EXAMPLE
                patient = Patient(name="Ben 10", age=10, gender="Male")
                patient.doctor = doctor_instance
                patient.insert()
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        delete(self)
            deletes a patient from the database

            EXAMPLE
                patient = Patient
                            .query
                            .filter(Patient.name == "Ben 10")
                            .first()
                patient.delete()
        """
        db.session.delete(self)
        db.session.commit()

    def update(self):
        """
        update(self)
            updates an existing patient information in the database

            EXAMPLE
                patient = Patient
                            .query
                            .filter(Patient.name == "Ben 10")
                            .first()
                patient.age = patient.age + 1
                patient.update()
        """
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.to_json())
