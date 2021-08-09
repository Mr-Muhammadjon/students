from django.shortcuts import redirect, render
from django.views.generic import View, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

class HomeView(LoginRequiredMixin,View):

    def get(self, request):
        teachers = Teacher.objects.all()
        students = Student.objects.all()
        
        context = {
            'teach':teachers,
            'count':len(teachers),
            'student':len(students)
        }
        return render(request, 'home.html', context)

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
    template_name = "students/registration.html"


class TeacherDetailView(DetailView):
    model = Teacher
    slug_field = 'slug'
    template_name = "det_teacher.html"
    ls = [1,100]
    nums = {'nums':ls}
    context_object_name = 'nums'


class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = Teacher
    fields = ['image','tel_num','subject','price']
    success_url = '/'
    template_name = "upd_teacher.html"

def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)

    context = {
        "students": paged_students
    }
    return render(request, "students/student_list.html", context)

