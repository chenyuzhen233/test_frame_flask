import os
import test_frame_api
import tempfile
import unittest


class ModuleTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_selectModuleById_01(self):
        params = {
            "id":1
        }
        response = self.app.post('/module/selectModuleById', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_selectModuleById_02(self):
        params = {
            "id":123456789
        }
        response = self.app.post('/module/selectModuleById', data=params)
        self.assertEqual(40001, response.json['code'])

    def test_post_selectModuleById_03(self):
        params = {
            "id":"asdasdasdasd"
        }
        response = self.app.post('/module/selectModuleById', data=params)
        self.assertEqual(40001, response.json['code'])

    def test_post_selectModuleById_04(self):
        params = {
            "id":""
        }
        response = self.app.post('/module/selectModuleById', data=params)
        self.assertEqual(40001, response.json['code'])

    def test_post_selectAllModule_01(self):
        params = {
            "token": "asd1234dfg"
        }
        response = self.app.post('/module/selectAllModule', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_selectAllModule_02(self):
        params = {
            "token": "123456"
        }
        response = self.app.post('/module/selectAllModule', data=params)
        self.assertEqual(20001, response.json['code'])

    def test_post_selectAllModule_03(self):
        params = {
            "token": ""
        }
        response = self.app.post('/module/selectAllModule', data=params)
        self.assertEqual(20002, response.json['code'])

    def test_post_selectAllModule_04(self):
        params = {
            "token": None
        }
        response = self.app.post('/module/selectAllModule', data=params)
        self.assertEqual(20002, response.json['code'])

    def test01_post_insertModule_01(self):
        params = {
            "name":"test",
            "project_id":1,
            "remarks":"just test"
        }
        response = self.app.post('/module/insertModule', data=params)
        self.assertEqual(00000, response.json['code'])
        ModuleTestCase.module_id = response.json['data']['id']

    def test_post_insertModule_02(self):
        params = {
            "name":"",
            "project_id": 1,
            "remarks":"just test"
        }
        response = self.app.post('/module/insertModule', data=params)
        self.assertEqual(40002, response.json['code'])

    def test_post_insertModule_03(self):
        params = {
            "name":None,
            "project_id": 1,
            "remarks":"just test"
        }
        response = self.app.post('/module/insertModule', data=params)
        self.assertEqual(40002, response.json['code'])

    def test02_post_deleteModuleById_01(self):
        params = {
            "id": ModuleTestCase.module_id
        }
        response = self.app.post('/module/deleteModuleById', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_deleteModuleById_02(self):
        params = {
            "id": ""
        }
        response = self.app.post('/module/deleteModuleById', data=params)
        self.assertEqual(40003, response.json['code'])

    def test_post_deleteModuleById_03(self):
        params = {
            "id": None
        }
        response = self.app.post('/module/deleteModuleById', data=params)
        self.assertEqual(40003, response.json['code'])

    def test_post_deleteModuleById_04(self):
        params = {
            "id": "test"
        }
        response = self.app.post('/module/deleteModuleById', data=params)
        self.assertEqual(40003, response.json['code'])


if __name__ == '__main__':
    unittest.main()