from django.db import models

from main.models import Subjects, Students


class WorkingOut(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, verbose_name='Предмет', related_name='working_out')
    student = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name='Студент', related_name='working_out')
    amount = models.PositiveIntegerField(verbose_name='Cумма')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'отработка'
        verbose_name_plural = 'отработки'

    def __str__(self):
        return self.student.middle_name
