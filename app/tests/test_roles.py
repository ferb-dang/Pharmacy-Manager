from .engine import EngineTestCase

class TestRoles (EngineTestCase):
    def setUp(self):
        super(TestRoles, self).setUp()

    def tearDown(self):
        super(TestRoles, self).tearDown()

    #Test read all roles in DB
    def test_read_roles(self):
        headers = self._get_authorization_headers()
        print ("haha" , headers)
        response = self.client.get(
            "/roles?skip=0&limit=200", headers=headers
        )
        assert response.status_code == 200

    #Test read a single role with given ID
    def test_read_role(self):
        headers = self._get_authorization_headers()
        response = self.client.get(
            f"/role/{self.data1['id']}", headers=headers
        )
        assert response.status_code == 200
