import os
import test_frame_api
import tempfile
import unittest


class InterfaceTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, test_frame_api.app.config['DATABASE'] = tempfile.mkstemp()
        test_frame_api.app.config['TESTING'] = True
        self.app = test_frame_api.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(test_frame_api.app.config['DATABASE'])

    def test_post_selectInterfaceById_01(self):
        params = {
            "id":1
        }
        response = self.app.post('/interface/selectInterfaceById', data=params)
        self.assertEqual(0000, response.json['code'])

    def test_post_selectInterfaceById_02(self):
        params = {
            "id":123456789
        }
        response = self.app.post('/interface/selectInterfaceById', data=params)
        self.assertEqual(50001, response.json['code'])

    def test_post_selectInterfaceById_03(self):
        params = {
            "id":"asdasdasdasd"
        }
        response = self.app.post('/interface/selectInterfaceById', data=params)
        self.assertEqual(50001, response.json['code'])

    def test_post_selectInterfaceById_04(self):
        params = {
            "id":""
        }
        response = self.app.post('/interface/selectInterfaceById', data=params)
        self.assertEqual(50001, response.json['code'])

    def test_post_selectAllInterface_01(self):
        params = {
            "token": "asd1234dfg"
        }
        response = self.app.post('/interface/selectAllInterface', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_selectAllInterface_02(self):
        params = {
            "token": "123456"
        }
        response = self.app.post('/interface/selectAllInterface', data=params)
        self.assertEqual(20001, response.json['code'])

    def test_post_selectAllInterface_03(self):
        params = {
            "token": ""
        }
        response = self.app.post('/interface/selectAllInterface', data=params)
        self.assertEqual(20002, response.json['code'])

    def test_post_selectAllInterface_04(self):
        params = {
            "token": None
        }
        response = self.app.post('/interface/selectAllInterface', data=params)
        self.assertEqual(20002, response.json['code'])

    def test01_post_insertInterface_01(self):
        params = {
            "name":"test",
            "module_id":1,
            "remarks":"just test"
        }
        response = self.app.post('/interface/insertInterface', data=params)
        self.assertEqual(00000, response.json['code'])
        InterfaceTestCase.interface_id = response.json['data']['id']

    def test_post_insertInterface_02(self):
        params = {
            "name":"",
            "module_id": 1,
            "remarks":"just test"
        }
        response = self.app.post('/interface/insertInterface', data=params)
        self.assertEqual(50002, response.json['code'])

    def test_post_insertInterface_03(self):
        params = {
            "name":None,
            "module_id": 1,
            "remarks":"just test"
        }
        response = self.app.post('/interface/insertInterface', data=params)
        self.assertEqual(50002, response.json['code'])

    def test02_post_deleteModuleById_01(self):
        params = {
            "id": InterfaceTestCase.interface_id
        }
        response = self.app.post('/interface/deleteInterfaceById', data=params)
        self.assertEqual(00000, response.json['code'])

    def test_post_deleteInterfaceById_02(self):
        params = {
            "id": ""
        }
        response = self.app.post('/interface/deleteInterfaceById', data=params)
        self.assertEqual(50003, response.json['code'])

    def test_post_deleteInterfaceById_03(self):
        params = {
            "id": None
        }
        response = self.app.post('/interface/deleteInterfaceById', data=params)
        self.assertEqual(50003, response.json['code'])

    def test_post_deleteInterfaceById_04(self):
        params = {
            "id": "test"
        }
        response = self.app.post('/interface/deleteInterfaceById', data=params)
        self.assertEqual(50003, response.json['code'])

if __name__ == '__main__':
    unittest.main()