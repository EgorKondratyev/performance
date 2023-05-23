from django.contrib import admin

from academic_performance.models import Speciality, Subjects, Students, Groups


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    pass
