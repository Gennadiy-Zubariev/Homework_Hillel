from django.db import models
from django.contrib.auth.models import User


class Members(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.user.username
