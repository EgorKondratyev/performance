from django.contrib.auth.views import LogoutView
from django.urls import path

from authorization.views import LoginUser
from work_out_and_performance.settings import LOGOUT_REDIRECT_URL

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='authentication/logout.html',
        next_page=LOGOUT_REDIRECT_URL
    ), name='logout')
]
