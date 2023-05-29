from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import Groups, Subjects, Students
from main.utils import BaseMixin
from academic_performance.utils import get_days
from academic_performance.models import AcademicPerformance


class GroupsView(BaseMixin, ListView):
    model = Groups
    template_name = 'performance/groups.html'
    context_object_name = 'groups'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GroupsView, self).get_context_data(
            **(kwargs | self.get_base_context_data(title='Выбор группы'))
        )
        return context

    def get_queryset(self):
        return Groups.objects.annotate().all()


class SubjectsView(BaseMixin, ListView):
    model = Subjects
    template_name = 'performance/subjects.html'
    context_object_name = 'subjects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SubjectsView, self).get_context_data(
            **(kwargs | self.get_base_context_data(title=f'Выбор предмета', group_id=self.kwargs['group_id']))
        )
        return context

    def get_queryset(self):
        return Subjects.objects.filter(groups__pk=self.kwargs['group_id'])


class PerformanceView(BaseMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('home')
    template_name = 'performance/performance.html'

    def get_context_performance(self, request, group_id: int, subject_id: int):
        year = int(request.GET.get('year', 2023))
        month = int(request.GET.get('month', 5))
        context = self.get_base_context_data(
            title='Успеваемость студентов',
            group_id=group_id,
            subject=Subjects.objects.get(pk=subject_id),
            students=Students.objects.filter(group_id=group_id).select_related(),
            days=get_days(year, month),
            year=year,
            month=month
        )
        return context

    def get(self, request, group_id: int, subject_id: int):
        context = self.get_context_performance(request, group_id, subject_id)
        return render(request, self.template_name, context)

    def post(self, request, group_id: int, subject_id: int):
        context = self.get_context_performance(request, group_id, subject_id)
        for data_about_mark, new_mark in request.POST.items():
            if not new_mark:
                new_mark = None
            if data_about_mark != 'csrfmiddlewaretoken':
                student_id, date = data_about_mark.split('_')
                try:
                    mark = AcademicPerformance.objects.get(
                        student_id=student_id,
                        subject_id=subject_id,
                        date=date
                    )
                    mark.mark = new_mark
                except AcademicPerformance.DoesNotExist:
                    mark = AcademicPerformance(date=date, student_id=student_id, subject_id=subject_id, mark=new_mark)
                mark.save()

        return render(request, self.template_name, context)
