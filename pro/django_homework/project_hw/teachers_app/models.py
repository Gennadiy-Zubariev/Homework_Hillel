from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Teacher(models.Model):
    full_teacher_name = models.CharField(max_length=100, verbose_name='ПІБ викладача')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Про викладача')
    photo = models.ImageField(upload_to='teachers_images', blank=True, null=True)
    specialties = models.CharField(max_length=200, blank=True, verbose_name='Спеціалізація(напрямок)')

    def __str__(self):
        return self.full_teacher_name


    class Meta:
        verbose_name = 'Викладач'
        verbose_name_plural = 'Викладачі'
        ordering = ['full_teacher_name']






