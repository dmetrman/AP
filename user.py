from flask import Blueprint, request, jsonify, Response
from flask_bcrypt import Bcrypt
from marshmallow import ValidationError
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from validation import UserSchema
from sqlalchemy import create_engine
from models import User, Order

user = Blueprint('user', __name__)
bcrypt = Bcrypt()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

session = Session()


@user.route('/users/', methods=['POST'])
def creatingUser():

    data = request.get_json(force=True)
    try:
        UserSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    session.query(User).filter_by(name=data['name']).first()

    exist = session.query(User).filter_by(username=data['username']).first()
    if exist:
        return Response(status=400, response="Username already exists")
    hashpassword = bcrypt.generate_password_hash(data['password'])
    users = User(name=data['name'], surname=data['surname'], username=data['username'], password=hashpassword)
    session.add(users)
    session.commit()
    session.close()
    return Response(response="User successfully created")


@user.route('/users/<id>', methods=['GET'])
def getUserById(id):
    id = session.query(User).filter_by(id=id).first()
    if not id:
        return Response(status=404, response="Id doesn't exist")
    biblethump = {'id': id.id, 'name': id.name, 'surname': id.surname, 'username': id.username}
    return jsonify({'user': biblethump})


@user.route('/users', methods=['GET'])
def getUsers():
    limbo = session.query(User)
    quer = [UserSchema().dump(i) for i in limbo]
    if not quer:
        return {"message": "No users available"}, 404
    res = {}
    for i in range(len(quer)):
        res[i + 1] = quer[i]
    return res


@user.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    data = request.get_json(force=True)
    try:
        UserSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    user_data = session.query(User).filter_by(id=id).first()
    if not user_data:
        return Response(status=404, response="Id doesn't exist")
    if 'name' in data.keys():
        session.query(User).filter_by(name=data['name']).first()

        user_data.name = data['name']

    if 'surname' in data.keys():
        session.query(User).filter_by(surname=data['surname']).first()

        user_data.surname = data['surname']

    if 'username' in data.keys():
        session.query(User).filter_by(username=data['username']).first()

        user_data.username = data['username']

    if 'password' in data.keys():
        hashpassword = bcrypt.generate_password_hash(data['password'])
        user_data.password = hashpassword

    session.commit()
    session.close()
    return Response(response="User successfully updated")


@user.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    id = session.query(User).filter_by(id=id).first()
    if not id:
        return Response(status=404, response="Id doesn't exist")
    exist = session.query(Order).filter_by(user_id=id.id).first()
    if exist:
        return Response(status=400, response="This user is a foreign key")
    session.delete(id)
    session.commit()
    session.close()
    return Response(response="User successfully deleted")