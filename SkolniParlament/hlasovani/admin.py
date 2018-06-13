from django.contrib import admin

# Register your models here.
from .models import Student,Kandidat,Vitezove,DataFile
admin.site.register(Student)
admin.site.register(Kandidat)
admin.site.register(Vitezove)
admin.site.register(DataFile)