from ..models import Attendance, Role, User


class AttendanceMixin:

    def create_role_if_not_exists(self, name: str = 'Cliente'):
        role_exists = Role.objects.filter(name=name).first()
        return role_exists if role_exists else Role.objects.create(name=name)

    def get_role(self, name: str = 'Cliente'):
        return Role.objects.filter(name=name).first()

    def create_user(
        self,
        first_name='Breno Carlos',
        last_name='Adalberto junior',
        email='breno@email.com',
        password='admin123',
        role_name=None
    ):
        role = self.create_role_if_not_exists(role_name)
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role
        )
    
    def create_attendance(self, doctor: User, client: User, is_finished=False):
        return Attendance.objects.create(
            doctor=doctor,
            client=client,
            is_finished=is_finished,
        )

    def make_attendace_in_batch(self, qtd: int = 10):
        doctor = self.create_user(
            first_name='Doutor aragão',
            last_name='pinheiro', 
            role_name='Doutor',
            email='doutor@email.com'
        )
        client = self.create_user(role_name='Cliente')

        attendances = []
        for i in range(qtd):
            attendances.append(self.create_attendance(doctor, client))
        
        return attendances
        