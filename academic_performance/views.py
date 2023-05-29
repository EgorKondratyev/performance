from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import Groups, Subjects, Students
from main.utils import BaseMixin
from academic_performance.utils import get_days


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
        return Groups.objects.annotate(amount_subjects=Count('subjects'), amount_sudents=Count('students')).all()


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

    def get(self, request, group_id: int, subject_id: int):
        context = self.get_base_context_data(
            title='Успеваемость студентов',
            subject=Subjects.objects.get(pk=subject_id),
            students=Students.objects.filter(group_id=group_id).select_related(),
            days=get_days(2023, 5)
        )

        return render(request, self.template_name, context)
