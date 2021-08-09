from .models import *

def students(request):
    context = {
        'student':Student.objects.all()
    }
    return context