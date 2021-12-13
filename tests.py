from sqlalchemy.orm import sessionmaker
import unittest

from base64 import b64encode
from app import app
import json
from models import User, Car, Order
from app import engine
from user import bcrypt

Session = sessionmaker(bind=engine)

class TestingBase(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    tester = app.test_client()
    session = Session()

    def tearDown(self):
        self.close_session()

    def close_session(self):
        self.session.close()

class ApiTest(TestingBase):
    car = {
        "brand": "bmw",
        "model": "b5",
        "status": "available"
    }

    user = {
        "name": "Valentin",
        "surname": "Kasparov",
        "username": "ValeraKasparov",
        "password": "12345678",
        "role": "user"
    }

    user1 = {
        "name": "Dmitriy",
        "surname": "Kuznecov",
        "username": "DimaKuznec",
        "password": "12345678",
        "role": "user"
    }

    order = {
        "user_id": 1,
        "car_id": 1,
        "beginningDate": "2021-09-09",
        "amountOfDays": "3",
        "complete": "successfully"
    }

    def test_User_Creation(self):
        response = self.tester.post("/users/", data=json.dumps(self.user),
                                    content_type='application/json')
        code = response.status_code
        self.assertEqual(200, code)
        self.session.query(User).filter_by(name='Valentin').delete()
        self.session.commit()

    def test_User_Creation_invalid(self):
        response = self.tester.post("/users/", data=json.dumps({
        "name": "Valenasdn",
        "surname": "Kasasdasd",
        "username": "ValeraKo",
        "password": "123",
        "role": "user"
    }), content_type="application/json")
        code = response.status_code
        self.assertEqual(400, code)

    def test_Get_User_By_id(self):
        hashpassword = bcrypt.generate_password_hash('12345678')
        user = User(id=123, name="Valentin", surname="Kasparov", username="Valerka", password=hashpassword, role="user")
        self.session.add(user)
        self.session.commit()
        response = self.tester.get('/users')
        code = response.status_code
        self.assertEqual(200, code)

    def test_Delete_User_by_Id(self):
        hashpassword = bcrypt.generate_password_hash('12345678')
        user = User(name='Dmitriy', surname='Kuznecov', username='DimaKuznechk', password=hashpassword, role='user')
        self.session.add(user)
        self.session.commit()
        response = self.tester.delete('/users/4')
        code = response.status_code
        self.assertEqual(401, code)


    def test_User_Creation_invaIid(self):
        response = self.tester.post("/users/", data=json.dumps({
        "name": "Barvaley",
        "surname": "Surnameha",
        "username": "Nononono",
        "password": "123",
        "role": "user"
    }), content_type="application/json")
        code = response.status_code
        self.assertEqual(400, code)




# python -m unittest tests.py