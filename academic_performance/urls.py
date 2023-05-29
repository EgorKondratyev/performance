from django.urls import path

from academic_performance.views import GroupsView, SubjectsView, PerformanceView

urlpatterns = [
    path('groups/', GroupsView.as_view(), name='groups'),
    path('subjects/<int:group_id>/', SubjectsView.as_view(), name='subjects'),
    path('<int:group_id>/<int:subject_id>/', PerformanceView.as_view(), name='performance')
]
