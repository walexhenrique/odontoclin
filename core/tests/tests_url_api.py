from django.test import SimpleTestCase
from django.urls import reverse


class CoreURLsAPITest(SimpleTestCase):
    def test_attendance_url_path_correct(self):
        url = reverse('core:attendance-list')
        self.assertEqual(url, '/api/v1/attendance/')
    