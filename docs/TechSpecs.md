# Technical Specifications

### Tech Stack

**Tools Used:**

   - Python (Backend) / JavaScript (Frontend)
   - SQLite (Development) / PostgreSQL (Production)
   - Python Libraries
       - Flask
       - Flask-SQLAlchemy
       - Flask-Migrate
       - python-dotenv
       - pytest
   - Javascript Libraries
       - React JS
       - antd
       - axios

### Database Models (or Tables)

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

### User Roles (Authentication Levels)
- Nurse -- Administers medication to the patient
    - read:patient
    - read:doctor
- Doctor -- Create and check the patient, assign and update patient medication
    - all of above
    - create:patient
    - update:patient
    - delete:patient
- Dean (Admin) -- Recruit a new doctor or update, fire an existing doctor
    - all of above
    - create:doctor
    - update:doctor
    - delete:doctor