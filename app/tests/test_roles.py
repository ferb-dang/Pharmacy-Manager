from fastapi.testclient import TestClient
import unittest
from main import app


client = TestClient(app)

class TestPermissions (unittest.TestCase):
    _token = None

    def setUp(self):
        self.data = {"id": "2"}
        self.login = {"user_name": "admin", "password": "admin"}

    def _get_access_token(self):
        if not self._token:
            res = client.post("/login", json=self.login)
            self._token = res.json()["access_token"]
        return self._token

    def _get_authorization_headers(self):
        return {"Authorization": f"Bearer {self._get_access_token()}"}

    def tearDown(self):
        pass

    def test_read_roles(self):
        headers = self._get_authorization_headers()
        response = client.get(
            "/roles?skip=0&limit=200", headers=headers
        )
        assert response.status_code == 200

    def test_read_role(self):
        headers = self._get_authorization_headers()
        response = client.get(
            f"/role/{self.data['id']}", headers=headers
        )
        assert response.status_code == 200

