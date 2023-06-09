from django.contrib import admin
from django.contrib.auth.models import Group, User

from main.models import Speciality, Subjects, Students, Groups


admin.site.site_header = 'Успеваемость и отработки'
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_abbreviated_name', 'qualification', 'study_period', 'admission_plan']
    list_display_links = ['pk', 'get_abbreviated_name']
    search_fields = ['name', 'get_abbreviated_name']
    search_help_text = 'Поиск возможен по полному и короткому имени специальности'

    @admin.display(description='Название')
    def get_abbreviated_name(self, field):
        return f'{field.abbreviated_name}'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'amount_subject_in_group']
    list_display_links = ['pk', 'name']
    search_fields = ['name']

    @admin.display(description='Количество групп, изучающих текущий предмет')
    def amount_subject_in_group(self, field):
        amount_groups = field.groups.count()
        if amount_groups == 0:
            return 'На данный момент никто не изучает текущий предмет'
        return amount_groups

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_full_name', 'city', 'group']
    list_display_links = ['pk', 'get_full_name']
    search_fields = ['middle_name', 'first_name', 'last_name']
    search_help_text = 'Поиск происходит по имени, фамилии И/ИЛИ отчеству'
    readonly_fields = ['get_user_id', 'get_full_name']
    fieldsets = (
        ('Основная информация', {
            'fields': ('first_name', 'middle_name', 'last_name', 'group')
        }),
        ('Дополнительная информация', {
            'classes': ('collapse', ),
            'fields': ('get_user_id', 'get_full_name', 'city', 'description',)
        })
    )

    @admin.display(description='ID')
    def get_user_id(self, field):
        return field.pk

    @admin.display(description='ФИО')
    def get_full_name(self, field):
        return f'{field.middle_name} {field.first_name} {field.last_name}'

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_speciality', 'form_of_education', 'course', 'get_amount_subjects', 'get_amount_students']
    list_filter = ['form_of_education', 'course']

    @admin.display(description='Специальность')
    def get_speciality(self, field):
        return f'{field.speciality.abbreviated_name}-{field.course}'

    @admin.display(description='Изучаемых предметов')
    def get_amount_subjects(self, field):
        return field.subjects.count()

    @admin.display(description='Студентов')
    def get_amount_students(self, field):
        return field.students.count()

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
