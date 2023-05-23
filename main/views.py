from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from main.utils import BaseMixin


class MainPageView(BaseMixin, LoginRequiredMixin, View):
    template_name = 'main/main_page.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        context = self.get_base_context_data(
            title='Главная страница'
        )
        return render(request, self.template_name, context)
