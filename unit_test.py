import unittest
import json
from app import app

class KeywordSearchVolumeTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hourly_subscription(self):
        payload = {
            "user_id": 2,
            "list_keywords": [3, 4],
            "timing": "hourly",
            "start_time": "2024-01-01T00:00:00",
            "end_time": "2024-01-02T23:59:59"
        }
        response = self.app.post('/query', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check the format and contents of the response
        self.assertIsInstance(data, list)
        for item in data:
            self.assertIn('keyword_id', item)
            self.assertIn('datetime', item)
            self.assertIn('search_volume', item)
            self.assertIn('timing', item)
            self.assertIsInstance(item['keyword_id'], int)
            self.assertIsInstance(item['datetime'], str)
            self.assertIsInstance(item['search_volume'], int)
            self.assertIn(item['timing'], ['hourly', 'daily'])

    def test_daily_subscription(self):
        payload = {
            "user_id": 1,
            "list_keywords": [1, 2],
            "timing": "daily",
            "start_time": "2024-01-01T00:00:00",
            "end_time": "2024-03-31T23:59:59"
        }
        response = self.app.post('/query', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)

        # Check the format and contents of the response
        self.assertIsInstance(data, list)
        for item in data:
            self.assertIn('keyword_id', item)
            self.assertIn('datetime', item)
            self.assertIn('search_volume', item)
            self.assertIn('timing', item)
            self.assertIsInstance(item['keyword_id'], int)
            self.assertIsInstance(item['datetime'], str)
            self.assertIsInstance(item['search_volume'], int)
            self.assertEqual(item['timing'], 'daily')

if __name__ == '__main__':
    unittest.main()
