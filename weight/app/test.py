import unittest
#from app import app
class BasicTestCase(unittest.TestCase):
        def test_home(self):
                tester = app.test_client(self)
                response = tester.get('/', content_type='html/text')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, b'Flask app - Blue team Weight ')
        def test_GET_health(self):
                tester = app.test_client(self)
                response = tester.get('/health', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'ok' in response.data)
        def test_GET_unknown(self):
                tester = app.test_client(self)
                response = tester.get('/unknown', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'Weight data is unavailable at the moment.' not in response.data)
        def test_POST_batch_weight(self):
                tester = app.test_client(self)
                response = tester.get('/batch-weight/test', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                print(response.data)
                self.assertTrue(b'Has been added to database.' in response.data)
        def test_GET_weight_weight(self):
                tester = app.test_client(self)
                response = tester.get('/weight', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'erorr db' not in response.data)
        def test_GET_item(self):
                tester = app.test_client(self)
                response = tester.get('item/2', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'erorr db' not in response.data)
        def test_GET_session(self):
                tester = app.test_client(self)
                response = tester.get('session/2', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'erorr db' not in response.data)
        def test_POST_weight_weight(self):
                tester = app.test_client(self)
                response = tester.get('/weight', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'erorr db' not in response.data)
if __name__ == '__main__':
    unittest.main()