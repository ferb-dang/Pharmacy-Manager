from passlib.context import CryptContext

from .engine import EngineTestCase

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRETKEY = "VoTmnFohfkzGnnFscDpM12"


class TestSignupLogin(EngineTestCase):
    def setUp(self):
        super(TestSignupLogin, self).setUp()
        self.login_data3 = {
            "user_name":"admin3",
            "password":"admin3"
        }

    def tearDown(self):
        super(TestSignupLogin, self).tearDown()

    #Hash password with secretkey
    def get_password(self, password):
        pwd_context.hash(password, salt=SECRETKEY)

    #Test signup with success code - success data
    def test_signup(self):
        response = self.client.post("/signup", json=self.signup1)
        assert response.status_code == 200

    #Test signup with duplicate username
    def test_signup_fail(self):
        response = self.client.post("/signup",json=self.signup1)
        assert response.status_code == 400

    #Test login with success data - success user_name and pass
    def test_login(self):
        response = self.client.post("/login", json=self.login_data1)
        assert response.status_code == 200
        assert response.json()['access_token']

    #Test login with fail data
    def test_login_fail(self):
        response = self.client.post("/login",json=self.login_data3)
        assert response.status_code == 400
        assert response.json()['detail'] == "Invalid login detail!"



