from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.html import escape
from .models import *

class CreateUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']


class CreateTeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['image','tel_num','subject','price']
        escape = ['user']


class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name','surname','image','tel_num','place','price']