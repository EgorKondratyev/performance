from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, View

from main.models import Groups, Subjects
from main.utils import BaseMixin


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
            **(kwargs | self.get_base_context_data(title=f'Выбор предмета'))
        )
        return context

    def get_queryset(self):
        return Subjects.objects.filter(groups__pk=self.kwargs['group_id'])

