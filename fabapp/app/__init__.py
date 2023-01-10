import logging
import requests
from app.index import MyIndexView
from flask import Flask, redirect
from flask_cors import CORS
from flask_appbuilder import AppBuilder, SQLA
from pprint import pprint

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
""" CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}}) """

@app.route('/')
def hello():
    return redirect("http://localhost:5000/homepage", code=302)

app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView, base_template='mytemplate.html')


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import models, views, api  # noqa