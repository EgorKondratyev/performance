from django.contrib.auth.views import LogoutView
from django.urls import path

from authorization.views import LoginUser

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='authentication/logout.html'), name='logout')
]
