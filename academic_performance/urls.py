from django.urls import path

from academic_performance.views import GroupsView

urlpatterns = [
    path('groups/', GroupsView.as_view(), name='groups')
]
