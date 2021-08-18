from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'main'

urlpatterns = [
    # user login
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", HomeView.as_view(), name="home"),
    
    path("add_teacher/", CreateTeacherView.as_view(), name="add_teacher"),
    path("add_student/", StudentCreateView.as_view(), name="add_student"),

    path("update_teacher/<pk>", TeacherUpdateView.as_view(), name="upd_teacher"),
    path("get_plus/<pk>", get_plus, name="get_plus"),
    path("came_student/<pk>", came_student, name="came_student"),
    path("payed_stu/<pk>", payed_stu, name="payed_stu"),
    path("history/<pk>", history_stu, name="history"),

    path('search/', liveSearch, name='search'),
]   