from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=300, null=True)
    full_description = models.TextField(null=True)
    image = models.ImageField(upload_to='courses_images', blank=True, null=True)
    current_users = models.ManyToManyField(User, blank=True, related_name='current_users')

    def __str__(self):
        return self.title
