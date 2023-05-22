from django.urls import path

from authorization.views import LoginUser

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
]
