from django.urls import path

from academic_performance.views import GroupsView, SubjectsView

urlpatterns = [
    path('groups/', GroupsView.as_view(), name='groups'),
    path('subjects/<int:group_id>/', SubjectsView.as_view(), name='subjects')
]
