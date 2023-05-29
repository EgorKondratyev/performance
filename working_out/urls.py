from django.urls import path

from working_out.views import WorkOutView

urlpatterns = [
    path('', WorkOutView.as_view(), name='work_out')
]
