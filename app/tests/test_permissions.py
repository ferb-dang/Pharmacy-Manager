from .engine import EngineTestCase


class TestPermissions (EngineTestCase):
    def setUp(self) -> None:
        return super(TestPermissions).setUp()

    def tearDown(self) -> None:
        return super(TestPermissions).tearDown()

    #Test read all permissions
    def test_read_permissions(self):
        headers = self._get_authorization_headers()
        response = self.client.get(
            "/Permissions?skip=0&limit=200", headers=headers
        )
        assert response.status_code == 200

    #Test read a single permission with given ID
    def test_read_permission(self):
        headers = self._get_authorization_headers()
        response = self.client.get(
            f"/Permissions/{self.data1['id']}", headers=headers
        )
        assert response.status_code == 200

