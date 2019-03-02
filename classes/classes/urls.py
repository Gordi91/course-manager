"""classes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teams.views import CreateCourseType, delete_course_type, CreateGroupType, delete_group, \
    CreateStudent, delete_student
from exams.views import CreateExam, delete_exam, CreateExercise, delete_exercise

urlpatterns = [
    path('admin/', admin.site.urls),
    path('types/delete/<int:type_id>/', delete_course_type, name='delete-type'),
    path('types/', CreateCourseType.as_view(), name='list-types'),
    path('groups/delete/<int:group_id>/', delete_group, name='delete-group'),
    path('groups/', CreateGroupType.as_view(), name='list-groups'),
    path('students/delete/<int:student_id>/', delete_student, name='delete-student'),
    path('students/', CreateStudent.as_view(), name='list-students'),
    path('exams/delete/<int:exam_id>/', delete_exam, name='delete-exam'),
    path('exams/', CreateExam.as_view(), name='list-exams'),
    path('exercises/delete/<int:exercise_id>/', delete_exercise, name='delete-exercise'),
    path('exercises/', CreateExercise.as_view(), name='list-exercises'),
    path('exam-result/')
]
