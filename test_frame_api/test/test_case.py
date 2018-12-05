#coding=utf-8
import os
import test_frame_api
import tempfile
import unittest


class CaseTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_selectCaseById_01(self):
        params = {
            "id":1
        }
        response = self.app.post('/case/selectCaseById', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_selectCaseById_02(self):
        params = {
            "id":123456789
        }
        response = self.app.post('/case/selectCaseById', data=params)
        self.assertEqual(60001, response.json['code'])

    def test_post_selectCaseById_03(self):
        params = {
            "id":"asdasdasdasd"
        }
        response = self.app.post('/case/selectCaseById', data=params)
        self.assertEqual(60001, response.json['code'])

    def test_post_selectCaseById_04(self):
        params = {
            "id":""
        }
        response = self.app.post('/case/selectCaseById', data=params)
        self.assertEqual(60001, response.json['code'])

    def test_post_selectAllCase_01(self):
        params = {
            "token": "asd1234dfg"
        }
        response = self.app.post('/case/selectAllCase', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_selectAllCase_02(self):
        params = {
            "token": "123456"
        }
        response = self.app.post('/case/selectAllCase', data=params)
        self.assertEqual(20001, response.json['code'])

    def test_post_selectAllTask_03(self):
        params = {
            "token": ""
        }
        response = self.app.post('/case/selectAllCase', data=params)
        self.assertEqual(20002, response.json['code'])

    def test_post_selectAllCase_04(self):
        params = {
            "token": None
        }
        response = self.app.post('/case/selectAllCase', data=params)
        self.assertEqual(20002, response.json['code'])

    def test01_post_insertCase_01(self):
        params = {
            "name": "test_case",
            "interface_id": 1,
            "method": 1,
            "params": "name:test|password:a123456",
            "url": "http://www.qq.com",
            "relation": "0",
            "relation_params": None,
            "save_params": None,
            "remarks": "just test"
        }
        response = self.app.post('/case/insertCase', data=params)
        self.assertEqual(00000, response.json['code'])
        CaseTestCase.case_id = response.json['data']['id']

    def test_post_insertCase_02(self):
        params = {
            "name":"",
            "interface_id": 1,
            "method": 1,
            "params": "name:test|password:a123456",
            "url": "http://www.qq.com",
            "relation": "0",
            "relation_params": None,
            "save_params": None,
            "remarks": "just test"
        }
        response = self.app.post('/case/insertCase', data=params)
        self.assertEqual(60002, response.json['code'])

    def test_post_insertCase_03(self):
        params = {
            "name":None,
            "interface_id": 1,
            "method": 1,
            "params": "name:test|password:a123456",
            "url": "http://www.qq.com",
            "relation": "0",
            "relation_params": None,
            "save_params": None,
            "remarks": "just test"
        }
        response = self.app.post('/case/insertCase', data=params)
        self.assertEqual(60002, response.json['code'])

    def test02_post_deleteCaseById_01(self):
        params = {
            "id": CaseTestCase.case_id
        }
        response = self.app.post('/case/deleteCaseById', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_deleteCaseById_02(self):
        params = {
            "id": ""
        }
        response = self.app.post('/case/deleteCaseById', data=params)
        self.assertEqual(60003, response.json['code'])

    def test_post_deleteCaseById_03(self):
        params = {
            "id": None
        }
        response = self.app.post('/case/deleteCaseById', data=params)
        self.assertEqual(60003, response.json['code'])

    def test_post_deleteCaseById_04(self):
        params = {
            "id": "test"
        }
        response = self.app.post('/case/deleteCaseById', data=params)
        self.assertEqual(60003, response.json['code'])


if __name__ == '__main__':
    unittest.main()