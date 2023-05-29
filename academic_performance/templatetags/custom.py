from django import template
from django.db.models import Avg

from main.models import Subjects, Students
from academic_performance.models import AcademicPerformance


register = template.Library()


@register.simple_tag(name='get_absolute_url_subject')
def get_absolute_url_subject(subject: Subjects, group_id: int):
    return subject.get_absolute_url(group_id=group_id)


@register.simple_tag(name='get_performance_days')
def get_performance_days(student: Students, subject: Subjects):
    dates = AcademicPerformance.objects.filter(student_id=student.pk, subject_id=subject.pk, mark__gte=1).values('date')
    result = [date['date'] for date in dates]
    return result


@register.simple_tag(name='get_mark')
def get_mark(student: Students, subject: Subjects, date):
    mark = AcademicPerformance.objects.get(student_id=student.pk, date=date, subject_id=subject.pk).mark
    return mark


@register.simple_tag(name='get_average_mark')
def get_average_mark(student: Students, subject: Subjects):
    average_mark = AcademicPerformance.objects.filter(
        student_id=student.pk, subject_id=subject.pk
    ).aggregate(average_mark=Avg('mark'))['average_mark']
    return average_mark if average_mark else 0


@register.inclusion_tag(filename='performance/dates_marks_students.html', name='dates_marks_students')
def dates_marks_students(days, student, subject):
    return {
        'days': days,
        'student': student,
        'subject': subject
    }
