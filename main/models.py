from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class Speciality(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название'
    )
    abbreviated_name = models.CharField(
        max_length=7,
        verbose_name='Сокращенное название',
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
            MaxValueValidator(6)
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

    def __str__(self):
        return self.abbreviated_name


class Subjects(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='Название'
    )

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):
        return self.name

    def get_absolute_url(self, group_id):
        return reverse('performance', kwargs={'group_id': group_id, 'subject_id': self.pk})


class Groups(models.Model):
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
    course = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ],
        verbose_name='Курс (стадия обучения)'
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
        return f'{self.speciality.abbreviated_name}-{self.course}'

    def get_absolute_url(self):
        return reverse('subjects', kwargs={'group_id': self.pk})


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
        """Добавляем студента только в том случае, если не достигнут максимальный план приема"""
        if Students.objects.filter(group_id=self.group_id).count() <= self.group.speciality.admission_plan:
            super().save(*args, **kwargs)
            return
        raise ValidationError('Достигнут максимальный план приема студентов')
