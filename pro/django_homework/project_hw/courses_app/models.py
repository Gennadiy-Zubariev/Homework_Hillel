from django.db import models
from teachers_app.models import Teacher
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600, null=True)
    program = models.TextField(null=True)
    image = models.ImageField(upload_to='courses_images', blank=True, null=True)
    start_date = models.DateField(verbose_name='Дата початку')
    end_date = models.DateField(verbose_name='Дата завершення')
    c_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rn_courses')
    c_teachers = models.ManyToManyField(Teacher, related_name='rn_courses', verbose_name='Викладачі')


    def __str__(self):
        return self.title


