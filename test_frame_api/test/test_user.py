import os
import test_frame_api
import unittest
import tempfile

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_selectUserById_01(self):
        params = {
            "id":1
        }
        response = self.app.post('/user/selectUserById', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_selectUserById_02(self):
        params = {
            "id":123456789
        }
        response = self.app.post('/user/selectUserById', data=params)
        self.assertEqual(10001, response.json['code'])

    def test_post_selectUserById_03(self):
        params = {
            "id":"asdasdasdasd"
        }
        response = self.app.post('/user/selectUserById', data=params)
        self.assertEqual(10001, response.json['code'])

    def test_post_selectUserById_04(self):
        params = {
            "id":""
        }
        response = self.app.post('/user/selectUserById', data=params)
        self.assertEqual(10001, response.json['code'])

if __name__ == '__main__':
    unittest.main()