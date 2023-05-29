from django import template

from main.models import Subjects, Students, Groups


register = template.Library()


@register.simple_tag(name='get_amount_student_in_group')
def get_amount_student_in_group(group: Groups):
    amount_student = group.students.count()
    return amount_student


@register.simple_tag(name='get_amount_subject_in_group')
def get_amount_subject_in_group(group: Groups):
    amount_subject = group.subjects.count()
    return amount_subject
