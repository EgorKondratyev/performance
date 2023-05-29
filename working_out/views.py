from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from main.utils import BaseMixin
from main.models import Students
from working_out.models import WorkingOut


class WorkOutView(BaseMixin, LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    template_name = 'work_out/show_student.html'

    def get(self, request):
        context = self.get_base_context_data(
            title='Отработки',
            working_out_all=WorkingOut.objects.all()
        )
        return render(request, self.template_name, context)
