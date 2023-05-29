from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from main.models import Students, Subjects


class AcademicPerformance(models.Model):
    date = models.DateField(verbose_name='Дата выставления отметки')
    mark = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        verbose_name='Отметка'
    )
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='performance', verbose_name='Студент')
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='performance', verbose_name='Предмет')
