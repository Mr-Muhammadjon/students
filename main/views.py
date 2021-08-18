from django.shortcuts import redirect, render
from django.views.generic import View, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from .forms import *
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
import datetime

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
        return render(request, 'teachers/create_teacher.html', context)

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
        return render(request, 'teachers/create_teacher.html', context)


class StudentCreateView(LoginRequiredMixin,CreateView):
    form_class = CreateStudentForm
    success_url = '/'
    template_name = "students/registration.html"


class TeacherDetailView(DetailView):
    model = Teacher
    slug_field = 'slug'
    template_name = "teachers/single_teacher.html"


class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    model = Teacher
    fields = '__all__'
    exclude = ['slug','date']
    success_url = '/all_teacher/'
    template_name = "teachers/edit_teacher.html"

class DeletTeacherView(DeleteView):
    model = Teacher
    template_name = 'teachers/teacher_list.html'
    success_url = '/all_teacher/'

def teacher_check(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    student = Student.objects.filter(teacher=teacher)
    context = {
        'teacher':teacher,
        'students':student,
    }
    return render(request, 'students/attendance_count.html', context)
# def student_came(request)

def student_list(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)

    context = {
        "students": paged_students
    }
    return render(request, "students/student_list.html", context)

def teacher_list(request):
    context = {'teachers':Teacher.objects.all()}
    return render(request,'teachers/teacher_list.html',context)

def historys(request,pk):
    h = History.objects.get(pk=pk)
    context = {
        'teachers':h,}
    return render(request, 'employee/histotys.html', context)



def get_plus(request):
    pk = request.GET.get('data')
    teacher = Teacher.objects.get(pk=pk)
    teacher.countsub += 1
    teacher.save()
    for i in teacher.student.all():
        i.came = False
        i.save()
    return JsonResponse({'status':200})

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
    return redirect(f'/check_student/{pk}')

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
    context = {
        'single_student':student,
    }
    return render(request, 'students/student_details.html', context)


def liveSearch(request):
    data = {}
    query = request.GET.get('data')
    history_came = list(History.objects.filter(time__icontains=query).values())
    data['history'] = history_came
    return JsonResponse(data)
