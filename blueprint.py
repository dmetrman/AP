from flask import Blueprint
from flask import Flask, request, jsonify
from wsgiref.simple_server import make_server
from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, User
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

api = Blueprint('api', __name__)

student_id = 30


@api.route(f'/hello-world-{student_id}')
def hello():
    return f'Hello World {student_id}'