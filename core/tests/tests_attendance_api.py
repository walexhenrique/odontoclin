from django.urls import reverse
from rest_framework.test import APITestCase

from .tests_attendance_api_base import AttendanceMixin


class AttendanceAPIv1Test(APITestCase, AttendanceMixin):

    def test_attendance_api_list_returns_status_200_OK(self):
        url = reverse('core:attendance-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
    def test_attendance_api_list_loads_correct_number_of_attendances(self):
        url = reverse('core:attendance-list')
        self.make_attendace_in_batch(qtd=11)

        response = self.client.get(url)
        qtd_load_attendance = len(response.data.get('results'))
        self.assertEqual(qtd_load_attendance, 10)

        response_page_number_2 = self.client.get(f'{url}?page=2')
        qtd_load_attendance_2 = len(response_page_number_2.data.get('results'))
        self.assertEqual(qtd_load_attendance_2, 1)
        