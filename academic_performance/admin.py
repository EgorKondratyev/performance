from django.contrib import admin

from academic_performance.models import Speciality, Subjects, Students, Groups


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_abbreviated_name', 'qualification', 'study_period', 'admission_plan']
    list_display_links = ['pk', 'get_abbreviated_name']
    search_fields = ['name', 'get_abbreviated_name']
    search_help_text = 'Поиск возможен по полному и короткому имени специальности'

    @admin.display(description='Название')
    def get_abbreviated_name(self, field):
        return field.abbreviated_name

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    pass
