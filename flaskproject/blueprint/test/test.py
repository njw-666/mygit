# import unittest
# from blueprint import createApp
# from settings import Config
# class MyTest(unittest.TestCase):
#     def setUp(self):
#         self.app=createApp(Config)
#         self.client=self.app.test_client()
#
#     def test_id(self):
#         resp=self.client.get("course/mydemo")
#         resp_code=resp.status_code
#
#         print(resp_code)
#         self.assertEqual(resp.status_code,200,"没有正常响应")
#         print(resp.data.decode())
#     def tearDown(self):
#         pass
#
#
# if __name__ == '__main__':
#     unittest.main()