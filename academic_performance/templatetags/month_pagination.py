import calendar

from django import template


register = template.Library()


@register.filter(name='feature_month')
def feature_month(month: int):
    if month == 12:
        return 1
    month += 1
    return month


@register.filter(name='feature_year')
def feature_year(year: int, month: int):
    if month == 12:
        return year + 1
    return year


@register.filter(name='last_month')
def last_month(month: int):
    if month == 1:
        return 12
    month -= 1
    return month


@register.filter(name='last_year')
def last_year(year: int, month: int):
    if month == 1:
        return year - 1
    return year


@register.simple_tag(name='get_month_name')
def get_month_name(month_number: int):
    return calendar.month_name[month_number]
