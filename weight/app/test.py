import unittest
from app import app
class BasicTestCase(unittest.TestCase):
        def test_home(self):
                tester = app.test_client(self)
                response = tester.get('/', content_type='html/text')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.data, b'Flask app - Blue team Weight ')
        def test_health(self):
                tester = app.test_client(self)
                response = tester.get('/health', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'ok' in response.data)
        def test_unknown(self):
                tester = app.test_client(self)
                response = tester.get('/unknown', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'Weight data is unavailable at the moment.' not in response.data)

        def test_batch_weight(self):
                tester = app.test_client(self)
                response = tester.get('/batch-weight/<file>', content_type='html/text')
                print(response.status_code)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(b'Weight data is unavailable at the moment.' not in response.data)

if __name__ == '__main__':
    unittest.main()