from django.db import models

# Create your models here.


class Exam(models.Model):
    course_type = models.ForeignKey(
        'teams.CourseType',
        verbose_name="Typ kursu",
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.CharField(
        verbose_name="Nazwa",
        max_length=100,
    )
    module_num = models.PositiveSmallIntegerField(
        verbose_name="Nr modułu"
    )

    def __str__(self):
        return f'{self.name}: {self.module_num}'

    class Meta:
        verbose_name = "Egzamin"
        verbose_name_plural = "Egzaminy"


class Exercise(models.Model):
    num = models.PositiveSmallIntegerField(
        verbose_name="Numer zadania"
    )
    points = models.PositiveSmallIntegerField(
        verbose_name="Punkty"
    )
    description = models.TextField(
        verbose_name="Treść zadania"
    )
    exam = models.ForeignKey(
        Exam,
        verbose_name="Egzamin",
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        if len(self.description) < 20:
            short_desc = self.description
        else:
            short_desc = self.description[0:20] + '...'
        return f'{self.exam.name}: {self.num} - {short_desc}'

    class Meta:
        verbose_name = "Zadanie"
        verbose_name_plural = "Zadania"


class ExerciseStudent(models.Model):
    student = models.ForeignKey(
        'teams.Student',
        verbose_name="Student",
        on_delete=models.CASCADE,
    )
    exercise = models.ForeignKey(
        Exercise,
        verbose_name="Zadanie",
        on_delete=models.CASCADE,
    )
    points = models.PositiveSmallIntegerField(
        verbose_name="Zdobyte punkty"
    )

    def __str__(self):
        return f'{self.student.github_nick}:{self.exercise.exam.module_num}:{self.exercise.num}'

    class Meta:
        verbose_name = "Zadanie zrobione przez studenta"
        verbose_name_plural = "Zadania zrobione przez studentów"
