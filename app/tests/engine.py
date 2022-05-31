from sqlalchemy import create_engine,MetaData,text
# from sqlalchemy.orm import sessionmaker
import os 
from pathlib import Path
from unittest import TestCase
from fastapi.testclient import TestClient

from core.config import DB_TEST_STRING
from main import app
import dbmodels


engine = create_engine(DB_TEST_STRING)


class EngineTestCase (TestCase):
    meta = MetaData()
    client = TestClient(app)
    _token = None
    

    #setUp some record for the test
    def setUp(self):
        #Setting a new database and connects
        dbmodels.Base.metadata.drop_all(engine)
        dbmodels.Base.metadata.create_all(engine)
        with engine.connect() as con:
            filename = os.path.join(Path(__file__).parent.parent,'db','permission.sql')
            with open(filename) as file:
                query = text(file.read())
                con.execute(query)

        #"self" with number 1 are exist in DB
        #"self" with number 2 are not exist in DB
        self.data1 = {
            "id": "1"
        }

        self.signup1 = {
            "role_id": "1",
            "user_name":"manager1",
            "password": "manager1"
        }
        
        self.login_data1 = {
            "user_name": "admin",
            "password": "admin"
        }

        self.create_medicine1 = {
            "name":"B",
            "medical_function":"bo sung vitamin B",
            "quantity":"1000",
            "price":"20000",
            "manufacture_date":"2022-05-05",
            "expire_date":"2022-05-05",
            "status":"out of stock"
        }

        self.update_medicine1 = {
            "name":"vitamin A",
            "medical_function":"bo sung vitamin A",
            "quantity":"700",
            "price":"876321762",
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
            "role_id": 2,
            "user_name": "pepper",
            "password": "123456",
            "name": "Thắng",
            "gender": 0,
            "date_of_birth": "1999-06-07",
            "email": "thangdv@vmodev.com",
            "address": "Hà Đông, Hà Lội",
            "phone_numbers": "091234567"
        }

    def _get_access_token(self):
        if not self._token:
            res = self.client.post("/login", json=self.login_data1)
            self._token = res.json()["access_token"]
        return self._token

    def _get_authorization_headers(self):
        return {"Authorization": f"Bearer {self._get_access_token()}"}

    #tearDown func to auto clean all the record after test
    def tearDown(self):
        dbmodels.Base.metadata.drop_all(engine)
        # ...
