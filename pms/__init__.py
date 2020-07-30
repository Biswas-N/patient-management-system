from flask import Flask, jsonify, render_template
from flask_cors import CORS

from pms.models import attach_db
from pms.utils import get_database_path, insert_dummy_data
from pms.api import attach_api

APP = Flask(
    __name__,
    static_folder='../client/build/static',
    template_folder='../client/build'
)
CORS(app=APP)

attach_db(app=APP, database_path=get_database_path(testing=False))
attach_api(app=APP)


# Below is an utility endpoint to insert sample data in the database
@APP.route("/refresh-db")
def refresh_db():
    insert_dummy_data()
    return jsonify({
        "success": True,
        "message": "Refreshed and populated databases"
    })


# The home page route, which serves the react application
@APP.route('/', defaults={'path': ''})
@APP.route('/<path:path>')
def index(path):
    return render_template("index.html")
