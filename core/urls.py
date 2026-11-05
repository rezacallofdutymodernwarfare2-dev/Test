from django.urls import path

from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path("login/", login_view, name="login"),
    ]
