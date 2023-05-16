from django.contrib import admin
from app.models import CustomUser
from app.models import Attendance
from app.models import Leave


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Attendance)
admin.site.register(Leave)

