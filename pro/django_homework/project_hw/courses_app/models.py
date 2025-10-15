from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600, null=True)
    program = models.TextField(null=True)
    image = models.ImageField(upload_to='courses_images', blank=True, null=True)

    def __str__(self):
        return self.title
