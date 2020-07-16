import os
import random
from dotenv import load_dotenv

from pms.models import db, Doctor, Patient


def get_database_path(testing: bool) -> str:
    """
    get_database_path(testing: bool)
        Creates a SQLAlchemy specific database path based on key-value pairs present in .env file
    """
    load_dotenv()

    if os.getenv("mode") == "Development":
        if testing:
            database_filename = "test_" + os.getenv("sqlite_filename")
        else:
            database_filename = os.getenv("sqlite_filename")
        project_dir = os.path.dirname(os.path.abspath(__file__))
        database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
        return database_path
    else:
        # TODO: Logic for PostgreSQL connection
        pass


def insert_dummy_data() -> None:
    """
    insert_dummy_data()
        (Only used for testing) Populates the database with 4 Doctors and 12 Patients. Patients are assigned to
        any one of the doctors randomly
    """
    db.drop_all()
    db.create_all()

    sample_doctors = [{"name": "Dr. Biswas", "age": 25},
                      {"name": "Dr. Batman", "age": 42},
                      {"name": "Dr. Who", "age": 125},
                      {"name": "Dr. Reed Richards", "age": 42}]

    for doctor in sample_doctors:
        temp_doctor = Doctor(name=doctor["name"], age=doctor["age"])
        temp_doctor.insert()

    sample_patients = [{"name": "Ben 10", "age": 10, "gender": "Male"},
                       {"name": "Gwen Stacy", "age": 20, "gender": "Female"},
                       {"name": "Barry Allen", "age": 23, "gender": "Male"},
                       {"name": "Arthur Curry", "age": 52, "gender": "Male"},
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"},
                       {"name": "Ben 10", "age": 10, "gender": "Male"},
                       {"name": "Gwen Stacy", "age": 20, "gender": "Female"},
                       {"name": "Barry Allen", "age": 23, "gender": "Male"},
                       {"name": "Arthur Curry", "age": 52, "gender": "Male"},
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"},
                       {"name": "Arthur Curry", "age": 52, "gender": "Male"},
                       {"name": "Selina Kyle", "age": 30, "gender": "Female"}]

    for patient in sample_patients:
        temp_patient = Patient(name=patient["name"], age=patient["age"], gender=patient["gender"])
        random_doctor = random.choice(sample_doctors)
        temp_patient.doctor = Doctor.query.filter(Doctor.name == random_doctor["name"]).first()

        temp_patient.insert()
