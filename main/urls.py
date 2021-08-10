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

    path("teacher/<slug>", TeacherDetailView.as_view(), name="det_teacher"),
    path("update_teacher/<pk>", TeacherUpdateView.as_view(), name="upd_teacher"),
    path("all_student/",student_list, name="all_student"),
    path("all_teacher/",teacher_list, name="all_teacher"),
    path("detail_student/<pk>",history_stu, name="single_detail"),
    path("delete/<pk>",DeletTeacherView.as_view(), name="delete"),
    path("check_student/<pk>", teacher_check, name="check"),
    path("came_student/<pk>", came_student, name="came_student"),
    path("get_plus/<pk>", get_plus, name="get_plus"),
    path("historys/<pk>", historys, name="historys"),
]   