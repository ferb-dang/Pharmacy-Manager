from .engine import EngineTestCase



class TestMedicine(EngineTestCase):
    def setUp(self) -> None:
        return super(TestMedicine).setUp()

    def tearDown(self) -> None:
        return super(TestMedicine).tearDown()

    #Test read all the medicines in db
    def test_read_medicines(self):
        headers = self._get_authorization_headers()
        response = self.client.get(
            "/medicines?skip=0&limit=200", headers=headers
        )
        assert response.status_code == 200

    #Test read medicine with given ID
    def test_read_medicine(self):
        headers = self._get_authorization_headers()
        response = self.client.get(f"/medicine/{self.data1['id']}", headers=headers)
        assert response.status_code == 200

    #Test read medicine with given ID but this id not exist
    def test_read_medicine_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.get(f"/medicine/{self.data2['id']}", headers=headers)
        assert response.status_code == 400

    #Test create medidcine with given data
    def test_create_medicine(self):
        headers = self._get_authorization_headers()
        response = self.client.post("/medicine",json=self.create_medicin2, headers=headers)
        assert response.status_code == 200

    #Test create medicine with duplicate user_name
    def test_create_medicine_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.post("/medicine",json=self.create_medicine1, headers=headers)
        assert response.status_code == 400    

    #Test update medicine with ID
    def test_update_medicine(self):
        headers = self._get_authorization_headers()
        response = self.client.put(f"/medicine/{self.data1['id']}", json=self.update_medicine1,headers=headers)
        assert response.status_code == 200

    #Test update medicine with unexist ID
    def test_update_medicine_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.put(f"/medicine/{self.data2['id']}", json=self.update_medicine1,headers=headers)
        assert response.status_code == 400

    #Test delete medicine with ID
    def test_delete_medicine(self):
        headers = self._get_authorization_headers()
        response = self.client.delete(f"/medicine/{self.data1['id']}",headers=headers)
        assert response.status_code == 200
        
    #Test delete medicine with unexist ID
    def test_delete_medicine_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.delete(f"/medicine/{self.data2['id']}",headers=headers)
        assert response.status_code == 404