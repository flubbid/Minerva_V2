from django.contrib import admin
from .models import Teacher, Student, Assignment
# Register your models here.
admin.site.Register(Teacher)
admin.site.Register(Student)
admin.site.Register(Assignment)