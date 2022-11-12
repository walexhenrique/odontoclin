from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True

class Role(BaseModel):
    name = models.CharField(max_length=45, default='Cliente', verbose_name='Cargo')
    def __str__(self) -> str:
        return self.name

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)

        if not Role.objects.filter(name='Cliente'):
            Role.objects.create().save()

        user.role = Role.objects.get(name='Cliente')
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)

        if not Role.objects.filter(name='Administrador'):
            Role.objects.create(name='Administrador').save()

        user.role = Role.objects.get(name='Administrador')
        user.save()
        return user

class User(AbstractUser):
    objects = UserManager()
    MARRIED = 'M'
    DIVORCIED = 'D'
    SINGLE = 'S'

    MARITAL_STATUS_CHOICES = [
        (MARRIED, 'Casado'),
        (DIVORCIED, 'Divorciado'),
        (SINGLE, 'Solteiro'),
    ]
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='core/covers/%Y/%m/%d/', blank=True, default='', verbose_name='Foto de perfil')
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, default=SINGLE, verbose_name='Status civil')
    birth_date = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')


class Attendance(BaseModel):
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Doutor', null=True, related_name='clients')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Cliente', null=True, related_name='doctors')
    is_finished = models.BooleanField(default=False, verbose_name='Atendido')
    
    def __str__(self) -> str:
        return f'{self.doctor} atendeu {self.client} em {self.created_at}'
