from flask import Blueprint

api = Blueprint('api', __name__)

student_id = 30


@api.route(f'/hello-world-{student_id}')
def hello():
    return f'Hello World {student_id}'