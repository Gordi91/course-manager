from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import CourseType, Group, Student
from django.shortcuts import redirect

# Create your views here.


class CreateCourseType(View):
    template_name = 'course_types.html'

    def get(self, request):
        types = CourseType.objects.all()
        return render(request, self.template_name, {
            'types': types,
        })

    def post(self, request):
        name = request.POST.get('name')
        if name:
            CourseType.objects.create(name=name)
        return self.get(request)


def delete_course_type(request, type_id):
    course_type = CourseType.objects.get(id=type_id)
    course_type.delete()
    return redirect(reverse('list-types'))


class CreateGroupType(View):
    template_name = 'groups.html'

    def get(self, request):
        types = CourseType.objects.all()
        groups = Group.objects.all()
        return render(request, self.template_name, {
            'types': types,
            'groups': groups,
        })

    def post(self, request):
        signature = request.POST.get('signature')
        course_type_id = request.POST.get('type')
        if signature and course_type_id:
            course_type = CourseType.objects.get(id=int(course_type_id))
            Group.objects.create(signature=signature, course_type=course_type)
        return self.get(request)


def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect(reverse('list-groups'))


class CreateStudent(View):
    template_name = 'students.html'

    def get(self, request):
        students = Student.objects.all()
        groups = Group.objects.all()
        return render(request, self.template_name, {
            'groups': groups,
            'students': students,
        })

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        github_nick = request.POST.get('github_nick')
        group_id = request.POST.get('group')
        if name and surname and email and github_nick and group_id:
            group = Group.objects.get(id=int(group_id))
            Student.objects.create(name=name, surname=surname, email=email, github_nick=github_nick, group=group)
        return self.get(request)


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect(reverse('list-students'))
