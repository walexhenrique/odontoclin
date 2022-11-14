from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('api/v1/attendance/', views.AttendanceAPIv1List.as_view(), name='attendance-list'),
    
]
