from flask import Flask, jsonify
from flask_cors import CORS

from pms.models import attach_db
from pms.utils import get_database_path, insert_dummy_data
from pms.api import attach_api

APP = Flask(__name__)
CORS(app=APP)

attach_db(app=APP, database_path=get_database_path(testing=False))
attach_api(app=APP)


# Below is an utility endpoint to insert sample data in the database
@APP.route("/insert-data")
def insert_data():
    insert_dummy_data()
    return jsonify({
        "success": True
    })
