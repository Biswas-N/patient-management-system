from flask import Flask
from flask_cors import CORS

from pms.models import attach_db
from pms.utils import get_database_path
from pms.api import attach_api

APP = Flask(__name__)
CORS(app=APP)

attach_db(app=APP, database_path=get_database_path(testing=False))
attach_api(app=APP)
