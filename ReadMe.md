# Patient Management System (PMS)
PMS is a full stack web application to manage patients and doctors record in a medical facility.

Built using [Flask](https://github.com/pallets/flask) (backend), [React](https://github.com/facebook/react) (frontend) and PostgreSQL. Information regarding detailed technical specifications can be found [here](./docs/TechSpecs.md).

## Installation
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

*Note: `.env.EXAMPLE` had bearer token variable which are needed during testing phase*

6. Finally, run these commands to start the application locally (uses SQLite, so no need for PostgreSQL config)
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