from .engine import EngineTestCase


class TestMedicine(EngineTestCase):
    def setUp(self) -> None:
        return super(TestMedicine).setUp()

    def tearDown(self) -> None:
        return super(TestMedicine).tearDown()
    

    #Test read 1 order with given ID
    def test_read_order(self):
        headers = self._get_authorization_headers()
        response = self.client.get(f"/order/{self.data1['id']}", headers=headers)
        assert response.status_code == 200

    #Test read 1 order with given ID fail
    def test_read_order_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.get(f"/order/{self.data2['id']}", headers=headers)
        assert response.status_code == 404

    #Test update 1 order with given ID
    def test_update_order(self):
        headers = self._get_authorization_headers()
        response = self.client.put(f"/order/{self.data1['id']}",json=self.update_order,headers=headers)
        assert response.status_code == 200

    #Test update 1 order with given ID fail
    def test_update_order_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.put(f"/order/{self.data2['id']}",json=self.update_order,headers=headers)
        assert response.status_code == 400

    #Test delete 1 order with given ID
    def test_delete_medicine(self):
        headers = self._get_authorization_headers()
        response = self.client.delete(f"/medicine/{self.data1['id']}",headers=headers)
        assert response.status_code == 200

    #Test delete 1 order with unexist ID
    def test_delete_medicine_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.delete(f"/medicine/{self.data3['id']}",headers=headers)
        assert response.status_code == 404
        