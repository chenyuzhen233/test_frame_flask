import os
import test_frame_api
import tempfile
import unittest


class ProjectTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_selectProjectById_01(self):
        params = {
            "id":1
        }
        response = self.app.post('/project/selectProjectById', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_selectProjectById_02(self):
        params = {
            "id":123456789
        }
        response = self.app.post('/project/selectProjectById', data=params)
        self.assertEqual(30001, response.json['code'])

    def test_post_selectProjectById_03(self):
        params = {
            "id":"asdasdasdasd"
        }
        response = self.app.post('/project/selectProjectById', data=params)
        self.assertEqual(30001, response.json['code'])

    def test_post_selectProjectById_04(self):
        params = {
            "id":""
        }
        response = self.app.post('/project/selectProjectById', data=params)
        self.assertEqual(30001, response.json['code'])

    def test_post_selectAllProject_01(self):
        params = {
            "token": "asd1234dfg"
        }
        response = self.app.post('/project/selectAllProject', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_selectAllProject_02(self):
        params = {
            "token": "123456"
        }
        response = self.app.post('/project/selectAllProject', data=params)
        self.assertEqual(20001, response.json['code'])

    def test_post_selectAllProject_03(self):
        params = {
            "token": ""
        }
        response = self.app.post('/project/selectAllProject', data=params)
        self.assertEqual(20002, response.json['code'])

    def test_post_selectAllProject_04(self):
        params = {
            "token": None
        }
        response = self.app.post('/project/selectAllProject', data=params)
        self.assertEqual(20002, response.json['code'])

    def test01_post_insertProject_01(self):
        params = {
            "name":"m5330-test",
            "remarks":"just test"
        }
        response = self.app.post('/project/insertProject', data=params)
        self.assertEqual(00000, response.json['code'])
        ProjectTestCase.project_id = response.json['data']['id']

    def test_post_insertProject_02(self):
        params = {
            "name":"",
            "remarks":"just test"
        }
        response = self.app.post('/project/insertProject', data=params)
        self.assertEqual(30002, response.json['code'])

    def test_post_insertProject_03(self):
        params = {
            "name":None,
            "remarks":"just test"
        }
        response = self.app.post('/project/insertProject', data=params)
        self.assertEqual(30002, response.json['code'])

    def test02_post_deleteProjectById_01(self):
        params = {
            "id": ProjectTestCase.project_id
        }
        response = self.app.post('/project/deleteProjectById', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_deleteProjectById_02(self):
        params = {
            "id": ""
        }
        response = self.app.post('/project/deleteProjectById', data=params)
        self.assertEqual(30003, response.json['code'])

    def test_post_deleteProjectById_03(self):
        params = {
            "id": None
        }
        response = self.app.post('/project/deleteProjectById', data=params)
        self.assertEqual(30003, response.json['code'])

    def test_post_deleteProjectById_04(self):
        params = {
            "id": "test"
        }
        response = self.app.post('/project/deleteProjectById', data=params)
        self.assertEqual(30003, response.json['code'])

if __name__ == '__main__':
    unittest.main()