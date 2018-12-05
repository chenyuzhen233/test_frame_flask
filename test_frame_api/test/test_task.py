#coding=utf-8
import os
import test_frame_api
import tempfile
import unittest


class TaskTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_selectTaskById_01(self):
        params = {
            "id":1
        }
        response = self.app.post('/task/selectTaskById', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_selectTaskById_02(self):
        params = {
            "id":123456789
        }
        response = self.app.post('/task/selectTaskById', data=params)
        self.assertEqual(70001, response.json['code'])

    def test_post_selectTaskById_03(self):
        params = {
            "id":"asdasdasdasd"
        }
        response = self.app.post('/task/selectTaskById', data=params)
        self.assertEqual(70001, response.json['code'])

    def test_post_selectTaskById_04(self):
        params = {
            "id":""
        }
        response = self.app.post('/task/selectTaskById', data=params)
        self.assertEqual(70001, response.json['code'])

    def test_post_selectAllTask_01(self):
        params = {
            "token": "asd1234dfg"
        }
        response = self.app.post('/task/selectAllTask', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_selectAllTask_02(self):
        params = {
            "token": "123456"
        }
        response = self.app.post('/task/selectAllTask', data=params)
        self.assertEqual(20001, response.json['code'])

    def test_post_selectAllTask_03(self):
        params = {
            "token": ""
        }
        response = self.app.post('/task/selectAllTask', data=params)
        self.assertEqual(20002, response.json['code'])

    def test_post_selectAllTask_04(self):
        params = {
            "token": None
        }
        response = self.app.post('/task/selectAllTask', data=params)
        self.assertEqual(20002, response.json['code'])

    def test01_post_insertTask_01(self):
        params = {
            "name": "test_task",
            "user_id": 1,
            "case_id": "1",
            "interface_id": 1,
            "project_id": 1,
            "host": "http://127.0.0.1:500",
            "remarks": "just test",
        }
        response = self.app.post('/task/insertTask', data=params)
        self.assertEqual(00000, response.json['code'])
        TaskTestCase.task_id = response.json['data']['id']

    def test_post_insertTask_02(self):
        params = {
            "name":"",
            "user_id": 1,
            "case_id": "1",
            "interface_id": 1,
            "project_id": 1,
            "host": "http://127.0.0.1:500",
            "remarks": "just test",
        }
        response = self.app.post('/task/insertTask', data=params)
        self.assertEqual(70002, response.json['code'])

    def test_post_insertTask_03(self):
        params = {
            "name":None,
            "user_id": 1,
            "case_id": "1",
            "interface_id": 1,
            "project_id": 1,
            "host": "http://127.0.0.1:500",
            "remarks": "just test",
        }
        response = self.app.post('/task/insertTask', data=params)
        self.assertEqual(70002, response.json['code'])

    def test02_post_deleteTaskById_01(self):
        params = {
            "id": TaskTestCase.task_id
        }
        response = self.app.post('/task/deleteTaskById', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_deleteTaskById_02(self):
        params = {
            "id": ""
        }
        response = self.app.post('/task/deleteTaskById', data=params)
        self.assertEqual(70003, response.json['code'])

    def test_post_deleteTaskById_03(self):
        params = {
            "id": None
        }
        response = self.app.post('/task/deleteTaskById', data=params)
        self.assertEqual(70003, response.json['code'])

    def test_post_deleteTaskById_04(self):
        params = {
            "id": "test"
        }
        response = self.app.post('/task/deleteTaskById', data=params)
        self.assertEqual(70003, response.json['code'])


if __name__ == '__main__':
    unittest.main()