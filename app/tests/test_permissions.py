from .engine import EngineTestCase


class TestPermissions (EngineTestCase):
    def setUp(self):
        super(TestPermissions, self).setUp()

    def tearDown(self):
        super(TestPermissions, self).tearDown()

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
            f"/Permission/{self.data1['id']}", headers=headers
        )
        print("hihi", self.data1['id'])
        assert response.status_code == 200
#
