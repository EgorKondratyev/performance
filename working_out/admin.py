from django.contrib import admin

from working_out.models import WorkingOut


@admin.register(WorkingOut)
class WorkingOutAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_full_name', 'subject', 'get_sum', 'date']
    list_display_links = ['pk', 'get_full_name']
    empty_value_display = 'Значение отсутствует'

    @admin.display(description='ФИО')
    def get_full_name(self, field):
        return f'{field.student.middle_name} {field.student.first_name} {field.student.last_name}'

    @admin.display(description='Сумма')
    def get_sum(self, field):
        return f'{field.amount} р.'
