from django.contrib import admin

from .models import Attendance, Role, User


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'client', 'is_finished']

admin.site.register(User)
admin.site.register(Role, RoleAdmin)
admin.site.register(Attendance, AttendanceAdmin)