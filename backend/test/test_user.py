from test.baseTest import BaseTest
from api.services.auth import user as userSVC
class TestUser(BaseTest):
    #----------------------------testcase----------------------
    # def test_get_exemple(self):
    #     response = self.client.get("/hello/")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json()['status'], 1)
    #     self.assertEqual(len(response.json()['message']), 0)

    def test_create_user_svc(self):
        from werkzeug.security import check_password_hash
        anUser = userSVC.User(
            username="jonathan",
            password="kiendrebeogo"
        )
        user = userSVC.create_user(anUser, self.db)
        assert user.username == anUser.username
        assert check_password_hash(user.password, anUser.password)
