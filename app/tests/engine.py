from sqlalchemy import create_engine,MetaData,engine
from sqlalchemy.orm import sessionmaker
from main import app
from unittest import TestCase
from fastapi.testclient import TestClient


from core.config import DB_TEST_STRING

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class EngineTestCase (TestCase):
    

    def setUp(self) -> None:
        self.token=""
        self._token = None
        self.meta = MetaData()
        self.engine = create_engine(DB_TEST_STRING)
        self.client = TestClient(app)

        #"self" with number 1 are exist in DB
        #"self" with number 2 are not exist in DB
        self.data1 = {
            "id": "1"
        }

        self.data2 = {
            "id": "100"
        }

        self.signup1 = {
            "role_id": "1",
            "user_name":"admin1",
            "password": "admin1"
        }
        self.signup2 = {
            "role_id": "1",
            "user_name":"admin2",
            "password": "admin2"
        }
        
        self.login_data1 = {
            "user_name": "admin1",
            "password": "admin1"
        }

        self.login_data2 = {
            "user_name": "admin2", 
            "password": "admin2"
        }

        self.login_data3 = {
            "user_name":"admin3",
            "password":"admin3"
        }

        self.create_medicine1 = {
            "name":"vitamin B",
            "medical_function":"bo sung vitamin B",
            "quantity":"1000",
            "price":"20000",
            "manufacture_date":"2022-05-05",
            "expire_date":"2022-05-05",
            "status":"out of stock"
        }

        self.create_medicine2 = {
            "name":"vitamin C",
            "medical_function":"bo sung vitamin C",
            "quantity":"656",
            "price":"876321",
            "manufacture_date":"2022-07-07",
            "expire_date":"2022-04-03",
            "status":"available"
        }

        self.update_medicine1 = {
            "name":"vitamin C",
            "medical_function":"bo sung vitamin C",
            "quantity":"700",
            "price":"8763217632",
            "manufacture_date":"2022-07-07",
            "expire_date":"2022-04-03",
            "status":"out of stock"
        }

        self.update_order = {
            "status":"pending",
            "shipping_address": "653, pending.st, ha noi",
            "shipping_fee": "10.000.000"
        }

        self.create_user1 = {
            "role_id": "2",
            "user_name": "pepper",
            "password": "123456",
            "name": "Thắng",
            "gender": "Male",
            "date_of_birth": "1999-06-07",
            "email": "thangdv@vmodev.com",
            "address": "Hà Đông, Hà Lội",
            "phone_numbers": "091234567"
        }

        self.create_user2 = {
            "role_id": "2",
            "user_name": "pepper",
            "password": "111111",
            "name": "Thắng Đặng",
            "gender": "Male",
            "date_of_birth": "1999-06-07",
            "email": "thang13576@gmail.com",
            "address": "Hà Đông, Hà Lội",
            "phone_numbers": "012345678"
        }

        self.create_user3 = {
            "role_id": "2",
            "user_name": "bumble bee",
            "password": "111111",
            "name": "Chi ong nau nau",
            "gender": "Female",
            "date_of_birth": "2000-11-29",
            "email": "chiongnau@gmail.com",
            "address": "Hà Đông, Hà Lội",
            "phone_numbers": "012345678"
        }
        
    def _get_access_token(self):
            if not self._token:
                res = self.client.post("/login", json=self.login)
                self._token = res.json()["access_token"]
            return self._token

    def _get_authorization_headers(self):
        return {"Authorization": f"Bearer {self._get_access_token()}"}
    

    def tearDown(self) -> None:
        ...



