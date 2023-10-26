from django.test import TestCase
# from unittest import TestCase
from rest_framework.test import APIClient


class TestSmth(TestCase):
    def test_sample_view_ok(self):
        client = APIClient()
        url = '/api/sensors/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
