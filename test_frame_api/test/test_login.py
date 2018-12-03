import os
import test_frame_api
import unittest
import tempfile


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_login_01(self):
        params = {
            "name":"test",
            "password":"123456"
        }
        response = self.app.post('/login/login', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_login_02(self):
        params = {
            "name":"test",
            "password":"asd"
        }
        response = self.app.post('/login/login', data=params)
        self.assertEqual(98001, response.json['code'])

    def test_post_login_03(self):
        params = {
            "name":"",
            "password":"asd"
        }
        response = self.app.post('/login/login', data=params)
        self.assertEqual(98001, response.json['code'])

    def test_post_login_04(self):
        params = {
            "name":None,
            "password":"asd"
        }
        response = self.app.post('/login/login', data=params)
        self.assertEqual(98001, response.json['code'])

    def test_post_logout_01(self):
        params = {
            "name":"test",
        }
        response = self.app.post('/login/logout', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_logout_02(self):
        params = {
            "name":"qwedvvxfg",
        }
        response = self.app.post('/login/logout', data=params)
        self.assertEqual(98002, response.json['code'])

    def test_post_logout_03(self):
        params = {
            "name":"",
        }
        response = self.app.post('/login/logout', data=params)
        self.assertEqual(98002, response.json['code'])

    def test_post_logout_04(self):
        params = {
            "name":None,
        }
        response = self.app.post('/login/logout', data=params)
        self.assertEqual(98002, response.json['code'])


if __name__ == '__main__':
    unittest.main()