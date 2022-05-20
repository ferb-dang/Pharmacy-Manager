from .engine import EngineTestCase




class TestPermissions (EngineTestCase):
    def setUp(self) -> None:
        return super(TestPermissions).setUp()

    def tearDown(self) -> None:
        return super(TestPermissions).tearDown()

    #Test read all roles in DB
    def test_read_roles(self):
        headers = self._get_authorization_headers()
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

