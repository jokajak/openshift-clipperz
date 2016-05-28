import os

from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from simplekv.db.sql import SQLAlchemyStore
from flask.ext.kvsession import KVSessionExtension

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_url_path='')
lm = LoginManager()
lm.init_app(app)
app.config.from_pyfile('../clipperz.cfg')
app.config['PROPAGATE_EXCEPTIONS'] = True
db = SQLAlchemy(app)
store = SQLAlchemyStore(db.engine, db.metadata, 'sessions')
kvsession = KVSessionExtension(store, app)

from clipperz import views, models, api
db.create_all()
