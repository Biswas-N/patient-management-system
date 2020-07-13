from flask import Flask

from .models import attach_db
from .utils import get_database_path
from .api import attach_api

APP = Flask(__name__)

attach_db(app=APP, database_path=get_database_path(testing=False))
attach_api(app=APP)
