from django import template

from main.models import Subjects


register = template.Library()


@register.simple_tag(name='get_absolute_url_subject')
def get_absolute_url_subject(subject: Subjects, group_id: int):
    return subject.get_absolute_url(group_id=group_id)
