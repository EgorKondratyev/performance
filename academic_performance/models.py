from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Speciality(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name='Название',
        unique=True
    )
    qualification = models.CharField(
        max_length=128,
        verbose_name='Квалификация'
    )
    study_period = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4)
        ],
        verbose_name='Период обучения'
    )
    admission_plan = models.IntegerField(
        default=20,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(40)
        ],
        verbose_name='План приема'
    )

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'специальности'


class Subjects(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'


class Groups(models.Model):
    abbreviated_name = models.CharField(
        max_length=7,
        verbose_name='Сокращенное название',
        unique=True
    )
    name = models.CharField(
        max_length=128,
        verbose_name='Название',
        unique=True
    )
    form_of_education_choices = (
        ('correspondence_abbreviated', 'Заочная сокращенная'),
        ('correspondence', 'Заочная'),
        ('full_time', 'Дневная')
    )
    form_of_education = models.CharField(
        max_length=40,
        choices=form_of_education_choices,
        default='full_time',
        verbose_name='Форма обучения'
    )
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.PROTECT,
        related_name='groups',
        verbose_name='Специальность'
    )
    subjects = models.ManyToManyField(
        Subjects,
        related_name='groups',
        verbose_name='Предметы'
    )

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.abbreviated_name


class Students(models.Model):
    first_name = models.CharField(
        max_length=24,
        verbose_name='Имя'
    )
    middle_name = models.CharField(
        max_length=40,
        verbose_name='Фамилия'
    )
    last_name = models.CharField(
        max_length=24,
        verbose_name='Отчество'
    )
    description = models.TextField(
        verbose_name='Дополнительная информация',
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город'
    )
    group = models.ForeignKey(
        Groups,
        on_delete=models.PROTECT,
        related_name='students',
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if Students.objects.count() <= self.group.speciality.admission_plan:
            super().save(*args, **kwargs)
        raise ValidationError('Достигнут максимальный план приема студентов')


class AcademicPerformance(models.Model):
    mark = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Отметка'
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='performance', verbose_name='Студен')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='performance', verbose_name='Предмет')
