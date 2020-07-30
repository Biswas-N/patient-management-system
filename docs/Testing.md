# Testing
Tools used for testing:
- [Postman](https://www.postman.com/downloads/) or [Newman](https://www.npmjs.com/package/newman) (Newman is a CLI replacement for Postman)
- [pytest](https://pypi.org/project/pytest/)

> *Note: Included bearer token are only valid for 24 hours. Thus bearer tokens needs to be refreshed after 24 hours.*

> *Token expires at **>Include date time<***

## Testing Production Deployment (in Heroku)

> Refresh the database **before** running any tests by opening this [link](https://patient-management-system-1603.herokuapp.com/refresh-db).

### Using Postman

1. Install **Postman** application using this [link](https://www.postman.com/downloads/).
2. Import the **Test Collection** and **Test Environment** by following these steps:
    1. Click the **Import** button on top-left part of your postman window (next to **New** button)
    2. Drag and drop the file `PMS.postman_collection.json` and `PMS.postman_environment.json` located in `tests/postman_tests`.
    3. Then hit **Import**
3. Head to collections tab and hover on the newly imported collection. Then press the right arrow and click **run**.
4. A **Collection Runner** pops up, then click **Run** (located in bottom left)

### Using Newman (Needs [NodeJS](https://nodejs.org/en/))

1. Install **Newman** using CLI with the command `npm install -g newman`
2. Lastly, execute the below command
    ```sh
    $ cd tests/postman_tests
    $ newman run -e PMS.postman_environment.json PMS.postman_collection.json
    ```

## Testing Local Deployment

### Using Pytest
1. Open a terminal in the **project root** and activate the virtual environment (created during local deployment)
    ```sh
    # For Windows
    > venv\Scripts\activate
    ```
    or
    ```sh
    # For Unix based (MacOS and Ubuntu)
    $ source venv/bin/activate
    ```
2. Update the `.env` file with latest bearer tokens for Dean, Doctor and Nurse role (if tokens are expired).
3. Then run the below command
    ```sh
    $ python -m pytest
    ```
> *Note: These tests will create a `test_database.db` file inside `pms` folder*