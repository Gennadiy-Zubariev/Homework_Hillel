from django.db import models
from django.contrib.auth.models import User
from courses_app.models import Courses


class Members(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(default='2000-01-01')
    courses = models.ManyToManyField(Courses, blank=True, related_name='members')

    def __str__(self):
        return self.user.username
