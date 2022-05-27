from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Docter_dep)

admin.site.register(DoctorModel)

admin.site.register(PatientModel)

admin.site.register(AppoinmentModel)
