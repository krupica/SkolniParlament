from django.contrib import admin

# Register your models here.
from .models import DataFile, Student, Kandidat, Vitezove

admin.site.register(DataFile)
admin.site.register(Student)
admin.site.register(Kandidat)
admin.site.register(Vitezove)