from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'main'

urlpatterns = [
    # user login
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # main
    path("", HomeView.as_view(), name="")
]   