from django.db.models import Count
from django.views.generic import ListView

from main.models import Groups
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
