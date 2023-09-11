from django.contrib import admin
from user.models import Users, Services, Patients

# Register your models here.

admin.site.register(Users)
admin.site.register(Services)
admin.site.register(Patients)

