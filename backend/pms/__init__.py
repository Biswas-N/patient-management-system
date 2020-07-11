from flask import Flask

from .models import attach_db
from .utils import get_database_path

APP = Flask(__name__)
attach_db(app=APP, database_path=get_database_path())


@APP.route("/")
def index():
    return "App Works!"
