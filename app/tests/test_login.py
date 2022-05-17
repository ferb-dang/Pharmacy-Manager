from fastapi.testclient import TestClient
from passlib.context import CryptContext

from core.config import SECRETKEY
from main import app

client = TestClient(app)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password(password):
    pwd_context.hash(password, salt=SECRETKEY)


def test_signup():
    singup_data= {
        "role_id": "1",
        "user_name": "admin2",
        "password": "admin2"
    }
    response = client.post("/signup",headers={"SECRET": "post"},json=singup_data)
    assert response.status_code==200
    assert response.json() == 





















































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


