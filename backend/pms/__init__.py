from flask import Flask

APP = Flask(__name__)


@APP.route("/")
def index():
    return "App Works!"
