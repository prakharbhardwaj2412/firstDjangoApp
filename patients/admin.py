from django.contrib import admin

# Register your models here.

from .models import PatientTable

admin.site.register(PatientTable)