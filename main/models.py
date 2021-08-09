from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

ls = ['1','2','3','4','5','6','7','8','9','0']

class Teacher(models.Model):
    user = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField("username", unique=True)
    image = models.ImageField("O'qituvchi rasmi", upload_to='teacher_img/', blank=True)
    tel_num = models.CharField("Telefon raqami", max_length=50, blank=True)
    # harajatlar hisobi
    subject = models.CharField("Qaysi fandan dars o'tishi", max_length=250)
    price = models.PositiveIntegerField("Bitta dars uchun narx", default=0)
    countsub = models.PositiveIntegerField("Bir oydagi darslar soni", default=0)
    allprice = models.PositiveIntegerField("Jami maosh", default=0)

    def __str__(self):
        return self.slug
    

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, related_name="student", on_delete=models.PROTECT)
    # shaxsiy ma'lumotlari
    name = models.CharField("Ismi", max_length=150)
    surname = models.CharField("Familiyasi", max_length=150)
    image = models.ImageField("O'quvchi rasmi", upload_to='student_img/', blank=True)
    tel_num = models.CharField("Telefon raqami", max_length=50, blank=True)
    place = models.CharField("Yashash manzili", max_length=50)
    # harajatlar hisobi
    price = models.PositiveIntegerField("Bitta dars uchun narx",default=0)
    countsub = models.PositiveIntegerField("Bir oydagi darslar soni",default=0)
    payed = models.BooleanField("to'lov qildi/qimadi", default=False)
    allprice = models.PositiveIntegerField("Jami to'lov",default=0)
    came = models.BooleanField("keldi/kemadi", default=False)

        
    def __str__(self):
        return self.name

    

class History(models.Model):
    student = models.ForeignKey(Student, related_name="history", on_delete=models.CASCADE)
    came_time = models.DateTimeField("Kelgan sanasi", auto_now_add=False)
    pay_time = models.DateTimeField("To'lov qilgan sanasi", auto_now_add=False)

    def __str__(self):
        return self.student.name
    