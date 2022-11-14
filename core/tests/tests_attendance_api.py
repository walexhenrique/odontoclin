from django.urls import reverse
from rest_framework.test import APITestCase

from .tests_attendance_api_base import AttendanceMixin


class AttendanceAPIv1Test(APITestCase, AttendanceMixin):

    def setUp(self) -> None:
        self.doctor = self.create_user(
            first_name='Doutor breno',
            last_name='Vargas',
            email='doutorbr@email.com',
            password='admin123',
            role_name='Doutor',
        )
        self.generic_client = self.create_user(
            first_name='Cliente bruno',
            last_name='macedo',
            email='clientebruno@email.com',
            password='admin123',
            role_name='Cliente'
        )
        return super().setUp()

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
    
    def test_attendance_api_list_loads_correct_attendances_querystring_finished_TRUE(self):
        url = reverse('core:attendance-list')
        self.make_attendace_in_batch(qtd=5, is_finished=True)
        self.create_attendance(self.doctor, self.generic_client, is_finished=False)
        
        response = self.client.get(f'{url}?finished=true')
        qtd_load_attendance = len(response.data.get('results'))
        self.assertEqual(qtd_load_attendance, 5)
    
    def test_attendance_api_list_loads_correct_attendances_querystring_finished_False(self):
        url = reverse('core:attendance-list')
        self.make_attendace_in_batch(qtd=5, is_finished=False)
        self.create_attendance(self.doctor, self.generic_client, is_finished=True)
        
        response = self.client.get(f'{url}?finished=false')
        qtd_load_attendance = len(response.data.get('results'))
        self.assertEqual(qtd_load_attendance, 5)




        