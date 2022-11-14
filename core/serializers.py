from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validations = []

    class Meta:
        model = Attendance
        fields = ['id', 'doctor', 'client', 'created_at', 'updated_at', 'is_finished']

    def validate_doctor(self, value):
        
        if str(value.role) != 'Doutor':
            self.validations.append('Doutor especificado não tem o cargo correspondente')

        return value

    def validate(self, attrs):
        if attrs.get('doctor') is None:
            self.validations.append('Doutor precisa ser especificado no atendimento')
        
        if attrs.get('client') is None:
            self.validations.append('Cliente precisa ser especificado no atendimento')

        super_validate = super().validate(attrs)

        if self.validations:
            raise ValidationError(self.validations)
        
        return super_validate
