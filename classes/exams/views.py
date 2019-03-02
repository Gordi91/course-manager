from django.shortcuts import render
from .models import Exam, Exercise, ExerciseStudent
from teams.models import CourseType, Student
from django.urls import reverse
from django.views import View
from django.shortcuts import redirect


class CreateExam(View):
    template_name = 'exams.html'

    def get(self, request):
        types = CourseType.objects.all()
        exams = Exam.objects.all()
        return render(request, self.template_name, {
            'types': types,
            'exams': exams,
        })

    def post(self, request):
        name = request.POST.get('name')
        module_num = request.POST.get('module_num')
        course_type_id = request.POST.get('type')
        if name and module_num and course_type_id:
            course_type = CourseType.objects.get(id=int(course_type_id))
            Exam.objects.create(name=name, course_type=course_type, module_num=module_num)
        return self.get(request)


def delete_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    exam.delete()
    return redirect(reverse('list-exams'))


class CreateExercise(View):
    template_name = 'exercises.html'

    def get(self, request):
        exercises = Exercise.objects.all()
        exams = Exam.objects.all()
        return render(request, self.template_name, {
            'exercises': exercises,
            'exams': exams,
        })

    def post(self, request):
        num = request.POST.get('num')
        points = request.POST.get('points')
        description = request.POST.get('description')
        exam_id = request.POST.get('exam_id')
        if num and points and description and exam_id:
            exam = Exam.objects.get(id=int(exam_id))
            Exercise.objects.create(num=num, points=points, description=description, exam=exam)
        return self.get(request)


def delete_exercise(request, exercise_id):
    exercise = Exercise.objects.get(id=exercise_id)
    exercise.delete()
    return redirect('list-exercises')


class CreateExerciseStudent(View):
    template_name = 'exercisestudent.html'

    def get(self, request):
        students = Student.objects.all()
        exercises = Exercise.objects.all()
        return render(request,self.template_name, {
            'students': students,
            'exercises': exercises
        })

    def post(self, request):
        num = request.POST.get('num')
        points = request.POST.get('points')
        students_points = request.POST.get('student_points')
        if num and points and students_points:
            ExerciseStudent.objects.create(num=num, points=points, students_points=students_points)
        return self.get(request)


def delete_exercise_student(request, exercise_student_id):
    exercise_student = ExerciseStudent.objects.get(id=int(exercise_student_id))
    exercise_student.delete()
    return redirect(reverse('list-exercisestudent'))
