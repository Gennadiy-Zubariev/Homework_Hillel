from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from courses_app.models import Courses


class Members(models.Model):
    m_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='rn_profile')
    m_courses = models.ManyToManyField(Courses, blank=True, related_name='rn_members')

    def __str__(self):
        return self.m_user.email
