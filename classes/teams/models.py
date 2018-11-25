from django.db import models


class CourseType(models.Model):
    name = models.CharField(
        verbose_name="Nazwa",
        max_length=30
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Typ kursu"
        verbose_name_plural = "Typy kursów"


class Group(models.Model):
    signature = models.CharField(
        verbose_name="Sygnatura",
        max_length=12
    )
    course_type = models.ForeignKey(
        CourseType,
        verbose_name="Typ kursu",
        on_delete=models.SET_NULL,
        null=True,
    )
    start_date = models.DateField(
        verbose_name='Data rozpoczęcia',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = "Grupa"
        verbose_name_plural = "Grupy"


class Student(models.Model):
    name = models.CharField(
        verbose_name="Imię",
        max_length=30,
    )
    surname = models.CharField(
        verbose_name="Nazwisko",
        max_length=60
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    github_nik = models.CharField(
        verbose_name="Nick na githubie",
        max_length=100
    )
    group = models.ForeignKey(
        Group,
        verbose_name="Grupa",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} {self.surname}: {self.github_nik}'

    class Meta:
        verbose_name = "Kursant"
        verbose_name_plural = "Kursanci"