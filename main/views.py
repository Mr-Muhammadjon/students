from django.shortcuts import redirect, render
from django.views.generic import View, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.http import JsonResponse
import datetime

# Create your views here.

class HomeView(LoginRequiredMixin,View):

    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            'teach':teachers,
        }
        return render(request, 'index.html', context)

class CreateTeacherView(LoginRequiredMixin, View):

    def get(self, request):
        form1 = CreateUser(request.GET)
        context = {
            'form1':form1,
        }
        return render(request, 'add_teacher.html', context)

    def post(self, request):
        form1 = CreateUser(request.POST)
        if form1.is_valid():
            user = form1.save()
            teacher = Teacher.objects.create(
                user=user,
                slug=user.username
            )
            teacher.save()
            return redirect('/')
        else:
            form1 = CreateUser()
        context = {
            'form1':form1,
        }
        return render(request, 'add_teacher.html', context)


class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    fields = ['teacher','name','surname','image','tel_num','place','price']
    success_url = '/'
    template_name = "add_student.html"


class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = Teacher
    fields = ['image','tel_num','subject','price']
    success_url = '/'
    template_name = "upd_teacher.html"


def get_plus(request, pk):
    # pk = request.GET.get('data')
    teacher = Teacher.objects.get(pk=pk)
    teacher.countsub += 1
    teacher.save()
    for i in teacher.student.all():
        i.came = False
        i.save()
    return redirect('/')

def came_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.came = True
    student.countsub += 1
    student.save()
    time_now = datetime.datetime.now().strftime('%D')
    history = History.objects.create(
        student=student,
        time=time_now,
    )
    history.save()
    return redirect('/')

def payed_stu(request, pk):
    student = Student.objects.get(pk=pk)
    student.payed = True
    payment = student.price * student.countsub
    student.save()
    time_now = datetime.datetime.now().strftime('%D')
    history = History.objects.create(
        student=student,
        payed=True,
        payed_money=payment,
        time=time_now,
    )
    history.save()
    return redirect('/')

def history_stu(request, pk):
    student = Student.objects.get(pk=pk)
    history = History.objects.filter(student=student)
    context = {
        'his':history,
        'stu':student,
    }
    return render(request, 'history.html', context)


def liveSearch(request):
    data = {}
    query = request.GET.get('data')
    history_came = list(History.objects.filter(time__icontains=query).values())
    data['history'] = history_came
    return JsonResponse(data)