from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceAPIv1List(ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    pagination_class = PageNumberPagination

    def get_finished(self):
        finished = self.request.GET.get('finished')
        if finished == 'true':
            return True

        return False

    def get_queryset(self):
        finished_exists = self.request.GET.get('finished')
        qs = super().get_queryset()

        if finished_exists:
            qs = qs.filter(is_finished=self.get_finished())
        
        return qs

class AttendanceAPIv1Detail(RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    pagination_class = PageNumberPagination

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_finished = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


