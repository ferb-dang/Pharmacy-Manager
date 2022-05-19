import unittest
from fastapi.testclient import TestClient
from passlib.context import CryptContext
from services import medicine_services

from app.main import app

client = TestClient(app)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRETKEY = "VoTmnFohfkzGnnFscDpM12"

class TestSignupLogin(unittest.TestCase):
    def setUp(self):
        self.data = {
            "role_id": "1",
            "user_name":"admin",
            "password": "admin"
        }

        self.login_data = {
            "user_name": "admin2", 
            "password": "admin2"
        }
        
    def tearDown(self):
        pass

    def get_password(self, password):
        pwd_context.hash(password, salt=SECRETKEY)

    #Test signup with success code - success data
    def test_signup(self):
        response = client.post("/signup", json=self.data)
        assert response.status_code == 200
        assert response.json()['access_token']

    #Test signup with duplicate username
    def test_signup_fail(self):
        response = client.post("/signup",json=self.data)
        assert response.status_code == 400

    #Test login with success code - success user_name and pass
    def test_login(self):
        response = client.post("/login", json=self.login_data)
        
        assert response.status_code == 200
        assert response.json()['access_token']

    #Test login with fail code
    def test_login_fail(self):
        login_data2 = {
            "user_name":"admin3",
            "password":"123456"
        }
        response = client.post("/login",json=login_data2)
        assert response.status_code == 400
        assert response.json()['detail'] == "Invalid login detail!"





# import requests

# from db.engine import create_session

# from .engine import EngineTestCase,app


# app.dependency_overrides[create_session] = EngineTestCase
# token = []

# class TestAuthen():
#     def setUp(self) -> None:
#         return super(TestAuthen,self).setUp()

#     def test_signup(self):
#         signup_data = {
#             'role_id':'1',
#             'user_name': 'admin1',
#             'password':'admin1'
#         }
#         response = requests.post("http://localhost:8000/signup",data=signup_data)

#         tokan = response.json()
#         assert response.status_code==200
#         assert "access_token" in tokan
#         assert tokan["access_token"]

#     def test_login(self):
#         login_data = {
#             'user_name': 'admin',
#             'password':'admin'
#         }
#         response = requests.post("http://localhost:8000/login", data=login_data)

#         tokan = response.json()
#         assert response.status_code == 200
#         assert "user_name" in tokan
#         assert "user_id" in tokan
#         assert "role" in tokan
