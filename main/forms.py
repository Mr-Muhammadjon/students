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
        fields = '__all__'
        


class CreateStudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
        