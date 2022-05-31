from .engine import EngineTestCase


class TestUser(EngineTestCase):
    def setUp(self):
        super(TestUser, self).setUp()
        self.data2 = {"id": "100"}

        self.create_user2 = {
            "role_id": "2",
            "user_name": "pepper",
            "password": "111111",
            "name": "Thắng Đặng",
            "gender": 1,
            "date_of_birth": "1999-06-07",
            "email": "thang13576@gmail.com",
            "address": "Hà Đông, Hà Lội",
            "phone_numbers": "012345678",
        }

        self.create_user3 = {
            "role_id": "2",
            "user_name": "bumble bee",
            "password": "111111",
            "name": "Chi ong nau nau",
            "gender": 0,
            "date_of_birth": "2000-11-29",
            "email": "chiongnau@gmail.com",
            "address": "Hà Đông, Hà Lội",
            "phone_numbers": "012345678",
        }

    def tearDown(self):
        super(TestUser, self).tearDown()

    # Test read all users in DB
    def test_read_users(self):
        headers = self._get_authorization_headers()
        response = self.client.get("/users", headers=headers)
        assert response.status_code == 200

    # Test read 1 user with given ID
    def test_read_user(self):
        headers = self._get_authorization_headers()
        response = self.client.get(f"/user/{self.data1['id']}", headers=headers)
        assert response.status_code == 200

    # Test read 1 user with unexist ID
    def test_read_user(self):
        headers = self._get_authorization_headers()
        response = self.client.get(f"/user/{self.data2['id']}", headers=headers)
        assert response.status_code == 404

    # Test create user with given data
    def test_create_user(self):
        headers = self._get_authorization_headers()
        response = self.client.post("/user", json=self.create_user1, headers=headers)
        assert response.status_code == 200

    # Test create user with duplicate username
    def test_create_user_case1(self):
        headers = self._get_authorization_headers()
        response = self.client.post("/user", json=self.create_user2, headers=headers)
        assert response.status_code == 400

    # Test create user with duplicate phone number
    def test_create_user_case2(self):
        headers = self._get_authorization_headers()
        response = self.client.post("/user", json=self.create_user3, headers=headers)
        assert response.status_code == 400

    # Test update user with given ID
    def test_update_user(self):
        headers = self._get_authorization_headers()
        response = self.client.put(
            f"/user/{self.data1['id']}", json=self.create_user1, headers=headers
        )
        assert response.status_code == 200

    # Test update user with unexist ID
    def test_update_user_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.put(
            f"/user/{self.data2['id']}", json=self.create_user1, headers=headers
        )
        assert response.status_code == 400

    # Test delete user with given id
    def test_delete_user(self):
        headers = self._get_authorization_headers()
        response = self.client.delete(f"/user/{self.data1['id']}", headers=headers)
        assert response.status_code == 200

    # Test delete user with unexist id
    def test_delete_user_fail(self):
        headers = self._get_authorization_headers()
        response = self.client.delete(f"/user/{self.data2['id']}", headers=headers)
        assert response.status_code == 404
