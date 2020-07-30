# Patient Management System (PMS)
PMS is a full stack web application to manage patients and doctors record in a medical facility.

> Deployed using Heroku at [link](http://patient-management-system-1603.herokuapp.com/).

Built using [Flask](https://github.com/pallets/flask) (backend), [React](https://github.com/facebook/react) (frontend) and PostgreSQL. Information regarding detailed technical specifications can be found [here](./docs/TechSpecs.md).

> The project's python code follows PEP8 Styling Guide

## Local Deployment
1. Clone this repository and move into the folder.
    ```sh
    $ git clone https://github.com/Biswas-N/patient-management-system.git
    $ cd patient-management-system
    ```
2. Create a virtual environment using [virtualenv](https://github.com/pypa/virtualenv) (Optional but advised).
    ```sh
    $ virtualenv venv
    ```
3. Activate the newly created virtual environment.
    ```sh
    # For Windows
    > venv\Scripts\activate
    ```
    or
    ```sh
    # For Unix based (MacOS and Ubuntu)
    $ source venv/bin/activate
    ```
4. Install the dependencies.
    ```sh
    $ pip install -r requirements.txt
    ```
5. Later, create a file called `.env` in the project root and copy-past the contents of `.env.EXAMPLE` into the `.env` file.

> *Note: `.env.EXAMPLE` had bearer token variable which are needed during testing phase*

6. Later run migrations to create a SQLite database file locally.
    ```sh
    $ python manage.py upgrade
    ```

7. Finally, run these commands to start the application locally (uses SQLite, so no need for PostgreSQL config)
    ```sh
    # For Windows
    > set FLASK_APP=pms
    > flask run
    ```
    or
    ```sh
    # For Unix based (MacOS and Ubuntu)
    $ export FLASK_APP=pms
    $ flask run
    ```

## Endpoints

This web application has two sets of CRUD endpoints to access Doctors and Patients. Detailed information and sample examples can be found [here](./docs/Endpoints.md)

## Testing

The application is deployed in [Heroku](https://www.heroku.com/). Thus, the tests are divided into two categories:    
1. Production Testsuit (Done using [postman](https://www.postman.com/))
2. Local Testsuit (Done using [Pytest](https://github.com/pytest-dev/pytest))

Detailed information on how to setup and executes these tests can be found [here](./docs/Testing.md)