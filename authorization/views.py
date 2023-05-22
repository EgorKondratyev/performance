from django.contrib.auth.views import LoginView

from authorization.forms import AuthenticationFormUser


class LoginUser(LoginView):
    form_class = AuthenticationFormUser
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        context = super(LoginUser, self).get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context
