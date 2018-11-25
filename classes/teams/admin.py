from django.contrib import admin
from .models import CourseType, Group, Student
# Register your models here.


@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
