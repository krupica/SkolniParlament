from django.contrib import admin

# Register your models here.
from .models import DataFile, Student

admin.site.register(DataFile)
admin.site.register(Student)