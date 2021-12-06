from flask import Flask, request, jsonify
from wsgiref.simple_server import make_server
from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, User
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from blueprint import api

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123456@localhost:5432/lab6'

with make_server('', 5000, app) as server:
    app.register_blueprint(api, url_prefix="/api/v30")
    server.serve_forever()

# curl -v -XGET http://localhost:5000/api/v1/hello-world-30
# http://127.0.0.1:5000/api/v1/hello-world-30

#alembic stamp head
#alembic revision --autogenerate
#alembic upgrade head