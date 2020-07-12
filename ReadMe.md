# Patient Management System
An open source Python's Flask and JavaScript's ReactJS based full stack application to manage patient records in a hospital.

## Technical Specifications

### Tech Stack

**Tools Used:**

   - Python (Backend) / JavaScript (Frontend)
   - SQLite (Development) / PostgreSQL (Production)

### Models

- Patient
    - id : Serial Integer
    - name : String
    - age : Integer
    - gender : Character
    - medication : String
    - doctor : Doctor

- Doctor
    - id : Serial Integer
    - name : String
    - age : Integer
    - patients : List of patients

*Note: A doctor can have **many** patients but a patient can only have **one** doctor*

### Roles

- Nurse - administers medication to the patient
    - read:patient
- Doctor - create and check the patient, assign and update patient medication
    - all of above
    - create:patient
    - update:patient
    - delete:patient
    - read:doctor
- Head Doctor (Admin) - CRUD a doctor
    - all of above
    - create:doctor
    - update:doctor
    - delete:doctor